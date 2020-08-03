from django.conf.urls import url
from api.views import *


urlpatterns = \
    [
        url(r'^task_list/$', TaskList.as_view(), name='task_list'),
        url(r'^create_task/$', CreateTask.as_view(), name='create_task'),
        url(r'^update_task/$', UpdateTask.as_view(), name='update_task'),
        url(r'^delete_task/$', DeleteTask.as_view(), name='delete_task'),
    ]