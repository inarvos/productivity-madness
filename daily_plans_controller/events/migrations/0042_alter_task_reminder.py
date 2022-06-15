# Generated by Django 4.0.4 on 2022-06-13 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0041_alter_task_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reminder',
            field=models.DurationField(blank=True, choices=[(datetime.timedelta(days=-7), 'Week before'), (datetime.timedelta(days=-2), '2 days before'), (datetime.timedelta(days=-1), '1 day before'), (datetime.timedelta(days=-1, seconds=75600), '3 hours before'), (datetime.timedelta(days=-1, seconds=82800), '1 hour before')], default=datetime.timedelta(0)),
        ),
    ]
