import json
from datetime import datetime

from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from decimal import Decimal, DecimalException
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import LimitOffsetPagination

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader

from rest_framework.views import APIView

from rest_framework import status
import re
from rest_framework.parsers import JSONParser

from task_manager.models import TasksList
from api.serializers import TasksListSerializer
# Create your views here.


class TaskList(generics.ListAPIView):
    queryset = TasksList.objects.all()
    serializer_class = TasksListSerializer


class CreateTask(APIView):

    def post(self, request, *args, **kwargs):
        data = self.request.data
        title = data.get('title', None)
        description = data.get('description', None)
        date_time = data.get('time_spend_task', None)
        if title and description and date_time:
            try:
                new_task = TasksList.objects.create(
                    title=title,
                    description=description,
                    time_spend_task=date_time
                )
                new_task.save()
                return Response({'response': 'Успешно'}, status=status.HTTP_200_OK)
            except ValidationError:
                return Response({
                    'message': 'Не верный формат даты'
                }, status=status.HTTP_400_BAD_REQUEST)
            except TasksList.DoesNotExist:
                return Response({
                            'message': 'Не удалось создать задачу'
                        }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Не верные данные'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateTask(APIView):

    def put(self, request, *args, **kwargs):
        data = self.request.data
        id = data.get('id', None)
        title = data.get('title', None)
        description = data.get('description', None)
        date_time = data.get('time_spend_task', None)
        return Response({'message': 'Не верные данные'}, status=status.HTTP_200_OK)


