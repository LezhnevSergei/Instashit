# Generated by Django 2.1 on 2020-01-18 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 18, 12, 0, 58, 521316, tzinfo=utc)),
        ),
    ]