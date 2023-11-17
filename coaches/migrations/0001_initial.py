# Generated by Django 3.0.6 on 2020-05-10 15:27

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('class_type', models.CharField(max_length=200)),
                ('info', models.TextField(blank=True)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(25)])),
                ('height', models.IntegerField(validators=[django.core.validators.MaxValueValidator(230), django.core.validators.MinValueValidator(160)])),
                ('hire_date', models.DateTimeField(default=datetime.datetime.now)),
                ('instagram_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
            ],
        ),
    ]