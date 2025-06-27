from django.contrib import admin
from .models import *

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name',)  # 관리자 목록에 이름만 보여줌
    search_fields = ('name',)  # 검색 필드 설정
