# Generated by Django 3.2.10 on 2022-12-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_task_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_pay',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
