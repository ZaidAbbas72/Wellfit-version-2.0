# Generated by Django 4.1.3 on 2023-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200724_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Images'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='display_filter_id',
            field=models.CharField(choices=[('buffet', 'Buffet'), ('gym', 'Gym Environment'), ('یوگا', 'یوگا'), ('بادی پامپ', 'بادی پامپ'), ('بدنسازی', 'بدنسازی'), ('تی آر ایکس', 'تی آر ایکس'), ('اسپینینگ', 'اسپینینگ'), ('فیتنس', 'فیتنس')], max_length=200),
        ),
    ]
