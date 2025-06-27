from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/index.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('details', views.detail, name='detail'),
    path('signup_done/', views.signup_done, name='signup_done'),
    path('delete_account', views.delete_account, name='delete_account'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
    path('edit/', views.edit_profile, name='edit'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html',success_url='/account/password_change_done/'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
]   