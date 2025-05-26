from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'building_ranking'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='building_ranking/index.html'), name='login'),
]