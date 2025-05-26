from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from . import views

app_name = 'about_server'

urlpatterns = [
    path('rule/', views.rule_main, name='rule'),
    path('join/', views.join_main, name='join'),
    path('description/', views.description_main, name='description'),
    #path('', views.about_server_main, name='about_server')
]