# Generated by Django 3.2.4 on 2021-07-17 09:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210717_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestedservice',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 17, 9, 59, 31, 123979, tzinfo=utc), verbose_name='Created on'),
        ),
    ]
