# Generated by Django 3.0.8 on 2020-08-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskslist',
            name='notification_sent',
            field=models.BooleanField(default=False, verbose_name='Уведомление было отправлено'),
        ),
    ]
