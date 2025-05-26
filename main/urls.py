from django.urls import path
from django.contrib.auth import views as auth_views
from .views import * # user>views에서 모든 함수를 가져온다.


app_name = 'main'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='main/index.html'), name='main'),
]