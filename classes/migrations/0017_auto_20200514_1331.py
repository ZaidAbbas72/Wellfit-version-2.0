# Generated by Django 3.0.6 on 2020-05-14 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0016_auto_20200514_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 14, 13, 31, 53, 662165)),
        ),
    ]