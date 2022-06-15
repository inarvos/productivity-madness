# Generated by Django 4.0.4 on 2022-06-13 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0034_alter_task_postponed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='reminder',
            field=models.DurationField(choices=[(datetime.timedelta(days=-7), 'Week before'), (datetime.timedelta(days=-2), '2 days before'), (datetime.timedelta(days=-1), '1 day before'), (datetime.timedelta(days=-1, seconds=75600), '3 hours before'), (datetime.timedelta(days=-1, seconds=82800), '1 hour before')], default=datetime.timedelta(days=-28)),
        ),
    ]
