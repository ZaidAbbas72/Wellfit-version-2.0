# Generated by Django 3.0.5 on 2020-07-15 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_gallery_display_filter_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Banner',
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'تصاویر'},
        ),
    ]