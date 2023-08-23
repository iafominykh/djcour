from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description', 'preview', 'is_publication')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

