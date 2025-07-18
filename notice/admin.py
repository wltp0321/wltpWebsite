from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect, get_object_or_404
from django.utils.html import format_html
from .models import ImportantNotice, NormalNotice, ArchivedNotice


def move_notice(request, from_model, to_model, pk):
    obj = get_object_or_404(from_model, pk=pk)
    to_model.objects.create(
        title=obj.title,
        content0=obj.content0,
        content1=obj.content1,
        created_at=obj.created_at,
    )
    obj.delete()
    messages.success(request, f"{from_model.__name__} → {to_model.__name__} 이동 완료")
    return redirect(f'/admin/notice/{to_model.__name__.lower()}/')


class ImportantNoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'move_actions')
    search_fields = ('id', 'title', 'content0', 'content1')
    ordering = ('-created_at',)

    def get_urls(self):
        urls = super().get_urls()  # 괄호 반드시 붙임
        custom_urls = [
            path('<int:pk>/move-to-normal/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, ImportantNotice, NormalNotice, pk)),
                name='move_to_normal'),
            path('<int:pk>/move-to-archive/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, ImportantNotice, ArchivedNotice, pk)),
                name='move_to_archive'),
        ]
        return custom_urls + urls

    def move_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">ToNormal</a> '
            '<a class="button" href="{}">ToArchive</a>',
            f'./{obj.pk}/move-to-normal/',
            f'./{obj.pk}/move-to-archive/',
        )
    move_actions.short_description = 'MoveTo'


class NormalNoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'move_actions')
    search_fields = ('id', 'title', 'content0', 'content1')
    ordering = ('-created_at',)

    def get_urls(self):
        urls = super().get_urls()  # 괄호 꼭 붙이기
        custom_urls = [
            path('<int:pk>/move-to-important/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, NormalNotice, ImportantNotice, pk)),
                name='move_to_important'),
            path('<int:pk>/move-to-archive/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, NormalNotice, ArchivedNotice, pk)),
                name='move_to_archive'),
        ]
        return custom_urls + urls

    def move_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">ToImportant</a> '
            '<a class="button" href="{}">ToArchive</a>',
            f'./{obj.pk}/move-to-important/',
            f'./{obj.pk}/move-to-archive/',
        )
    move_actions.short_description = 'MoveTo'


class ArchivedNoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'move_actions')
    search_fields = ('id', 'title', 'content0', 'content1')
    ordering = ('-created_at',)

    def get_urls(self):
        urls = super().get_urls()  # 괄호 필수
        custom_urls = [
            path('<int:pk>/move-to-important/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, ArchivedNotice, ImportantNotice, pk)),
                name='move_to_important'),
            path('<int:pk>/move-to-normal/', self.admin_site.admin_view(
                lambda request, pk: move_notice(request, ArchivedNotice, NormalNotice, pk)),
                name='move_to_normal'),
        ]
        return custom_urls + urls

    def move_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">ToImportant</a> '
            '<a class="button" href="{}">ToNormal</a>',
            f'./{obj.pk}/move-to-important/',
            f'./{obj.pk}/move-to-normal/',
        )
    move_actions.short_description = 'MoveTo'


admin.site.register(ImportantNotice, ImportantNoticeAdmin)
admin.site.register(NormalNotice, NormalNoticeAdmin)
admin.site.register(ArchivedNotice, ArchivedNoticeAdmin)
