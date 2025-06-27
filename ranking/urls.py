from django.urls import path
from . import views

app_name = 'ranking'

urlpatterns = [
    path('', views.ranking_main, name='ranking'),
    path('build_ranking/', views.build_ranking_main, name='build_ranking'),
    path('redstone_ranking/', views.redstone_player_ranking_main, name='redstone_ranking'),
    path('hard_worked_ranking/', views.hard_worked_player_ranking_main, name='hard_worked_ranking'),
]
