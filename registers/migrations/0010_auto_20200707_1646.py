# Generated by Django 3.0.5 on 2020-07-07 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0009_auto_20200707_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='expiration_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 7, 7), null=True),
        ),
    ]
