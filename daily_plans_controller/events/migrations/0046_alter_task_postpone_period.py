# Generated by Django 4.0.4 on 2022-06-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0045_alter_task_postpone_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='postpone_period',
            field=models.CharField(choices=[('Days', 'Weeks')], max_length=20),
        ),
    ]
