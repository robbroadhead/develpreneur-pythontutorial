# Generated by Django 3.1.2 on 2020-11-13 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpproject', '0003_auto_20201113_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completiondate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='duedate',
            field=models.DateTimeField(null=True),
        ),
    ]
