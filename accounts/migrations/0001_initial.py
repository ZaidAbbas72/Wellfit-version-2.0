# Generated by Django 3.0.6 on 2020-05-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/%Y/%m/%d')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Banner',
            },
        ),
    ]
