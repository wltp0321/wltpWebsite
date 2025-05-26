from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login, get_user_model
from account.forms import UserForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token


# Create your views here.
def account_main(request):
    return render(request, "account/index.html")

def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 비밀번호 확인도 같다면
        if request.POST['username'] is not None:
            if request.POST['password1'] == request.POST['password2']:

                
                # 유저 만들기
                user = User.objects.create_user(
                                    username=request.POST['username'],
                                    password=request.POST['password1'],
                                    email=request.POST['email'],
                                    first_name=request.POST['nickname0'],
                                    last_name=request.POST['nickname1'])
                user.is_active = False # 유저 비활성화
                user.save()


                current_site = get_current_site(request) 
                message = render_to_string('account/activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                mail_title = "계정 활성화 확인 이메일"
                mail_to = request.POST["email"]
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()
                return redirect("account:signup_done")

    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'account/signup.html')



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("/")
    else:
        return render(request, 'base.html', {'error' : '계정 활성화 오류'})


def signup_done(request):
    return render(request, 'account/signup_succfully.html')
  
def delete_account(request):
    if request.method == "POST":
        password = request.POST.get("password")

        user = authenticate(username=request.user.username, password=password)
        if user:
            request.user.delete()      # 사용자 삭제
            logout(request)            # 세션 종료
            messages.success(request, "회원 탈퇴가 완료되었습니다.")
            return redirect("main")    # 홈으로 리디렉션
        else:
            messages.error(request, "비밀번호가 일치하지 않습니다.")

    return render(request, "account/delete_account.html")

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:detail')  # 수정 후 이동할 페이지
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'account/edit_profile.html', {'form': form})


def detail(request):
    return render(request, 'account/accounts.html')