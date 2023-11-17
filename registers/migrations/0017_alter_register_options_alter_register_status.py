# Generated by Django 4.1.3 on 2023-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0016_auto_20200716_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name_plural': 'Registrations'},
        ),
        migrations.AlterField(
            model_name='register',
            name='status',
            field=models.CharField(choices=[('Created', 'Created'), ('Paid', 'Paid')], default='Created', max_length=120),
        ),
    ]
