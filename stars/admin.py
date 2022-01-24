from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class StarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'time_create', 'photo', 'is_published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'get_html_photo', 'photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Star, StarAdmin)
admin.site.register(models.Category, CategoryAdmin)

admin.site.site_title = 'Шоураннеры, актрисы, актеры'
admin.site.site_header = 'Шоураннеры, актрисы, а также актеры'
