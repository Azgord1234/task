from django.contrib import admin
from .models import TasksList


@admin.register(TasksList)
class TasksList(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)
    list_display = ('title', 'time_spend_task',)
