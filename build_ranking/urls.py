from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'build_ranking'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='build_ranking/index.html'), name='login'),
]