from django.contrib import admin

from main.models import Customer, Message, Mailing, Attempt


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname',)
    list_filter = ('fullname',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('message', 'mailing_time', 'frequency', 'status',)
    list_filter = ('frequency', 'mailing_time', 'status',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'time_mailing', 'status', 'server_response',)
    list_filter = ('mailing', 'time_mailing', 'status', 'server_response',)
