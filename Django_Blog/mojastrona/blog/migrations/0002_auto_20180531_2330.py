# Generated by Django 2.0.2 on 2018-05-31 21:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentarz',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 21, 30, 14, 600893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_utworzenia',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 31, 21, 30, 14, 600893, tzinfo=utc)),
        ),
    ]
