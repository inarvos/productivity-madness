# Generated by Django 4.0.4 on 2022-06-10 20:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_alter_task_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='postponed',
            field=models.CharField(blank=True, choices=[(datetime.timedelta(days=1), 'One day'), (datetime.timedelta(days=3), 'Three days'), (datetime.timedelta(days=7), 'One week'), (datetime.timedelta(days=14), 'Two weeks'), (datetime.timedelta(days=28), 'One month')], max_length=20, null=True),
        ),
    ]
