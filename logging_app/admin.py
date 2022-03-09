from django.contrib import admin
from .models import LoggingModel


@admin.register(LoggingModel)
class LoggingModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'model_name', 'record_id', 'create_date', 'action')
    readonly_fields = ('create_date',)
    ordering = ('-create_date', )
    search_fields = ('user__username',)
    list_filter = ('model_name', 'action', )
