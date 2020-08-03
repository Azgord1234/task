from celery import Celery
# Инициализация Celery
app = Celery(broker='redis://localhost:6379', backend='redis://localhost:6379')
app.autodiscover_tasks()
