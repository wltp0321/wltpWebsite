# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('important_notices/', views.important_notices, name='important_notices'),
    path('normal_notices/', views.normal_notices, name='normal_notices'),
    path('archived_notices/', views.archived_notices, name='archived_notices'),
]
