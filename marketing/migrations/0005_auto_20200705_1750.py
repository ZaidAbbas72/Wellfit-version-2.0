# Generated by Django 3.0.5 on 2020-07-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0004_guestmarketing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestmarketing',
            name='guest_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
