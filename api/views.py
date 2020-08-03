import json
from datetime import datetime, timedelta

from django.core.exceptions import ValidationError
from rest_framework import status, filters, generics
from rest_framework.response import Response

from rest_framework.views import APIView

from task_manager.models import TasksList
from api.serializers import TasksListSerializer
# Create your views here.


class TaskList(generics.ListAPIView):
    queryset = TasksList.objects.all()
    serializer_class = TasksListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
        range_param = self.request.query_params.get('time_range', None)
        if range_param == 'week':
            time_range = datetime.now() - timedelta(weeks=1)
        elif range_param == 'day':
            time_range = datetime.now() - timedelta(days=1)
        elif range_param == 'month':
            # берем за месяц 30 дней
            time_range = datetime.now() - timedelta(days=30)
        else:
            return queryset
        queryset = queryset.filter(time_spend_task__gte=time_range)
        return queryset


class CreateTask(APIView):

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.data)
        title = data.get('title', None)
        description = data.get('description', None)
        date_time = data.get('date_time', None)
        if title and description and date_time:
            try:
                new_task = TasksList.objects.create(
                    title=title,
                    description=description,
                    time_spend_task=date_time
                )
                new_task.save()
                return Response({'response': 'Успешно создано'}, status=status.HTTP_200_OK)
            except ValidationError:
                return Response({
                    'message': 'Не верный формат данных'
                }, status=status.HTTP_400_BAD_REQUEST)
            except TasksList.DoesNotExist:
                return Response({
                            'message': 'Не удалось создать задачу'
                        }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Не верные данные'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateTask(APIView):

    def put(self, request, *args, **kwargs):
        data = json.loads(self.request.data)
        pk = data.get('id', None)
        title = data.get('title', None)
        description = data.get('description', None)
        date_time = data.get('date_time', None)
        if pk and title and description and date_time:
            try:
                task = TasksList.objects.get(pk=pk)
                task.title = title
                task.description = description
                task.time_spend_task = date_time
                task.save()
                return Response({'response': 'Успешно обновлено'}, status=status.HTTP_200_OK)
            except ValidationError:
                return Response({
                    'message': 'Не верный формат данных'
                }, status=status.HTTP_400_BAD_REQUEST)
            except TasksList.DoesNotExist:
                return Response({
                            'message': 'Не удалось обновить задачу'
                        }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Не верные данные'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteTask(APIView):

    def delete(self, request, *args, **kwargs):
        data = json.loads(self.request.data)
        pk = data.get('id', None)
        if pk:
            try:
                task = TasksList.objects.get(pk=pk)
                task.delete()
                return Response({'response': 'Успешно'}, status=status.HTTP_200_OK)
            except TasksList.DoesNotExist:
                return Response({
                            'message': 'Не удалось удалить задачу'
                        }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Не верные данные'}, status=status.HTTP_400_BAD_REQUEST)


