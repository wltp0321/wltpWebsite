from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name='list'),
    path('archived/<int:notice_id>/', views.archived_notice, name='archived_notice'),
]
