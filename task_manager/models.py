from django.db import models


# Create your models here.

class TasksList(models.Model):
    title = models.CharField(verbose_name='Заголовок задачи', max_length=2000)
    description = models.TextField(verbose_name='Описание задачи', max_length=3000)
    time_spend_task = models.DateTimeField(verbose_name='Время проведения задачи')
    notification_sent = models.BooleanField(verbose_name='Уведомление было отправлено', default=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Список задач'
