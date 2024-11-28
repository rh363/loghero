from django.contrib import admin

from loghero.models import *

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'ip_address',
        'location',
        'actor',
        'action',
        'severity',
        'status',
        'target',
        'target_type',
        'created_at',
    )
    list_filter = (
        'severity',
        'status',
    )
    search_fields = (
        'id',
        'actor',
        'action',
        'severity',
        'status',
        'target',
        'target_type',
        'created_at',
        'ip_address',
        'user_agent',
        'location',
        'url',
        'result',
        'result_type',
        'description',
        'extra_data',
        'created_at',
    )