# Generated by Django 4.0.4 on 2022-06-18 14:13

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_notification_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('repeatable', models.DurationField(choices=[(datetime.timedelta(days=1), 'Daily'), (datetime.timedelta(days=7), 'Weekly'), (datetime.timedelta(days=28), 'Monthly'), (datetime.timedelta(days=365), 'Yearly')], default=datetime.timedelta(days=28))),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='start',
        ),
    ]