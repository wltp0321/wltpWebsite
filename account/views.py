from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login, get_user_model
from account.forms import UserForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse
# 이메일 관련
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.conf import settings

User = get_user_model()


def account_main(request):
    return render(request, "account/index.html")


def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # ✅ UID + 토큰 생성
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)

            # ✅ 계정 활성화 링크 생성
            activation_link = f"{settings.SITE_URL}{reverse('account:activate', kwargs={'uidb64': uid, 'token': token})}"

            # ✅ HTML 템플릿 렌더링 (여기가 핵심)
            html_content = render_to_string('account/activation_email.html', {
                'user': user,
                'activation_link': activation_link,
            })

            # ✅ 이메일 전송
            email = EmailMessage(
                subject="IMPERIUM SERVER 계정 활성화 안내",
                body=html_content,
                to=[user.email],
            )
            email.content_subtype = "html"  # HTML 형식으로 전송
            email.send()

            return render(request, 'account/signup_succfully.html', {'email': user.email})
    else:
        form = UserForm()
    return render(request, 'account/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'account/activation_failed.html')  # 따로 오류 페이지 만들어도 좋음


def signup_done(request):
    return render(request, 'account/signup_succfully.html')


@login_required
def delete_account(request):
    if request.method == "POST":
        password = request.POST.get("password")
        user = authenticate(username=request.user.username, password=password)

        if user:
            request.user.delete()
            logout(request)
            messages.success(request, "회원 탈퇴가 완료되었습니다.")
            return redirect("main")
        else:
            messages.error(request, "비밀번호가 일치하지 않습니다.")

    return render(request, "account/delete_account.html")


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:detail')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'account/edit_profile.html', {'form': form})


@login_required
def detail(request):
    return render(request, 'account/accounts.html')
