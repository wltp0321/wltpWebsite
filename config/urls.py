"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from django.views.static import serve
from django.urls import re_path as url

from . import views
from main.views import main_main
from gallery.views import gallery_main
from build_ranking.views import build_ranking_main
from building_ranking.views import building_ranking_main
from redstone_ranking.views import redstone_ranking_main
from command_ranking.views import command_ranking_main
from account.views import account_main
from rule.views import server_rule
from how_to_join.views import server_how_to_join
from description.views import server_descriptions



urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', main_main, name='main'),  # 메인 페이지
path('ads.txt',views.Ads),
    path('building_ranking/', building_ranking_main, name='building_ranking'),
    path('gallery/', gallery_main, name='gallery'),
    path('build_ranking/', build_ranking_main, name='build_ranking'),
    path('redstone_ranking/', redstone_ranking_main, name='redstone_ranking'),
    path('command_ranking/', command_ranking_main, name='command_ranking'),
    path('rules/', server_rule, name='rule'),
    path('descriptions/', server_descriptions, name='descriptions'),
    path('how_to_join/', server_how_to_join, name='how_to_join'),
    path('notices/', include('notice.urls')),
    path('account/', include("account.urls")),  # account 앱 포함
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


def redirect_to_main(request, exception):
    return redirect("main")

handler404 = redirect_to_main

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)