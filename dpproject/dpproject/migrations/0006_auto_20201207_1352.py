# Generated by Django 3.1.2 on 2020-12-07 13:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dpproject', '0005_auto_20201113_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completiondate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Completed Date'),
        ),
        migrations.AlterField(
            model_name='task',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Due'),
        ),
        migrations.AlterField(
            model_name='task',
            name='minutes_spent',
            field=models.IntegerField(blank=True, help_text='Minutes spent working this task', null=True, verbose_name='Time Spent'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, help_text='Name of the task', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpproject.lkpstatus', verbose_name='Status'),
        ),
    ]
