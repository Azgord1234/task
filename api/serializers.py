from rest_framework import serializers, fields

from task_manager.models import TasksList


class TasksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksList
        fields = '__all__'
