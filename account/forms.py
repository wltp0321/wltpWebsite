from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
        labels = {
            'username': _('사용자 이름'),
            'password1': _('비밀번호'),
            'password2': _('비밀번호 확인'),
            'email': _('이메일'),
        }
        help_texts = {
            'username': _('필수! 문자, 숫자, @/./+/-/_ 만 사용할 수 있습니다.'),
        }
        error_messages = {
            'username': {
                'required': _('사용자 이름은 필수입니다.'),
                'unique': _('이미 존재하는 사용자 이름입니다.'),
            },
            'email': {
                'invalid': _('유효한 이메일 주소를 입력하세요.'),
                'required': _('이메일은 필수입니다.'),
            },
            'password2': {
                'password_mismatch': _('비밀번호가 일치하지 않습니다.'),
            },
        }



class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        labels = {
            'username': _('사용자 이름'),
            'email': _('이메일'),
            'first_name': _('마인크래프트 계정 1'),
            'last_name': _('마인크래프트 계정 2'),
        }
        help_texts = {
            'username': _('필수! 문자, 숫자, @/./+/-/_ 만 사용할 수 있습니다.'),
        }
        error_messages = {
            'username': {
                'required': _('사용자 이름은 필수입니다.'),
                'unique': _('이미 존재하는 사용자 이름입니다.'),
            },
            'email': {
                'invalid': _('유효한 이메일 주소를 입력하세요.'),
                'required': _('이메일은 필수입니다.'),
            },
        }
