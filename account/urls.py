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
    path('delete_account', views.delete, name='delete_account'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name="activate"),
]