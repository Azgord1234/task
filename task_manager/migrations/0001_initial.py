# Generated by Django 3.0.8 on 2020-08-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TasksList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000, verbose_name='Заголовок задачи')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание задачи')),
                ('time_spend_task', models.DateTimeField(verbose_name='Время проведения задачи')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Список задач',
                'verbose_name_plural': 'Список задач',
            },
        ),
    ]
