from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'redstone_ranking'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='redstone_ranking/index.html'), name='login'),
]