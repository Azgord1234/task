from celery import shared_task

from tasks import settings
from .models import TasksList
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template import loader


@shared_task
def send_notification():
    tasks = TasksList.objects.filter(notification_sent=False)
    if tasks.exists():
        for item in tasks:
            if item.time_spend_task - timedelta(hours=1) <= datetime.now():
                try:
                    mail_data = {
                        'title': item.title,
                        'description': item.description,
                        'time_spend_task': item.time_spend_task,
                        'id': item.pk,
                    }
                    email_message = EmailMultiAlternatives('Уведомление о событии', '',
                                                           'почта с которой будет отправлена форма',
                                                           ['почта получается'])

                    html_email = loader.render_to_string('notification.html', mail_data)
                    email_message.attach_alternative(html_email, 'text/html')
                    email_message.send()
                    item.notification_sent = True
                    item.save()
                except Exception as exc:
                    print('Ошибка', exc)
