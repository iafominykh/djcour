from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'full_name', 'comment', 'image')
    list_filter = ('full_name',)
    search_fields = ('email', 'full_name',)
