# Generated by Django 4.0.6 on 2022-07-06 19:40

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('repeatable', models.DurationField(choices=[(datetime.timedelta(days=1), 'Daily'), (datetime.timedelta(days=7), 'Weekly'), (datetime.timedelta(days=28), 'Monthly'), (datetime.timedelta(days=365), 'Yearly')], default=datetime.timedelta(days=28))),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('duration', models.DurationField(choices=[(datetime.timedelta(seconds=7200), 'Two hours'), (datetime.timedelta(seconds=10800), 'Three hours'), (datetime.timedelta(seconds=21600), 'Six hours'), (datetime.timedelta(seconds=43200), 'Twelve hours'), (datetime.timedelta(days=1), 'One day')], default=datetime.timedelta(seconds=3600))),
                ('reminder', models.DurationField(choices=[(datetime.timedelta(days=-28), 'Month before'), (datetime.timedelta(days=-14), '2 weeks before'), (datetime.timedelta(days=-7), '1 week before'), (datetime.timedelta(days=-3), '3 days before'), (datetime.timedelta(days=-1), '1 day before'), (datetime.timedelta(days=-1, seconds=75600), '3 hours before'), (datetime.timedelta(days=-1, seconds=82800), '1 hour before')], default=datetime.timedelta(days=-28))),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('repeatable', models.DurationField(choices=[(datetime.timedelta(days=1), 'Daily'), (datetime.timedelta(days=7), 'Weekly'), (datetime.timedelta(days=28), 'Monthly'), (datetime.timedelta(days=365), 'Yearly')], default=datetime.timedelta(days=28))),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('done', models.BooleanField(default=False)),
                ('done_at', models.DateTimeField(null=True)),
                ('archived', models.BooleanField(default=False)),
                ('postponed', models.DurationField(blank=True, choices=[(datetime.timedelta(days=1), 'One day'), (datetime.timedelta(days=3), 'Three days'), (datetime.timedelta(days=7), 'One week'), (datetime.timedelta(days=14), 'Two weeks'), (datetime.timedelta(days=28), 'One month')], null=True)),
                ('deadline_reminder', models.DurationField(blank=True, choices=[(datetime.timedelta(days=-7), 'Week before'), (datetime.timedelta(days=-2), '2 days before'), (datetime.timedelta(days=-1), '1 day before'), (datetime.timedelta(days=-1, seconds=75600), '3 hours before'), (datetime.timedelta(days=-1, seconds=82800), '1 hour before')], null=True)),
                ('postponed_reminder', models.DurationField(blank=True, choices=[(datetime.timedelta(days=-7), 'Week before'), (datetime.timedelta(days=-2), '2 days before'), (datetime.timedelta(days=-1), '1 day before'), (datetime.timedelta(days=-1, seconds=75600), '3 hours before'), (datetime.timedelta(days=-1, seconds=82800), '1 hour before')], null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.task')),
            ],
        ),
    ]