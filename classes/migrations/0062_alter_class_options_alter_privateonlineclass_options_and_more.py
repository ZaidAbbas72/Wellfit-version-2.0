# Generated by Django 4.1.3 on 2023-11-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0061_auto_20200715_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'In-Person Classes'},
        ),
        migrations.AlterModelOptions(
            name='privateonlineclass',
            options={'verbose_name_plural': 'Private Online Classes'},
        ),
        migrations.AlterModelOptions(
            name='publiconlineclass',
            options={'verbose_name_plural': 'Public Online Classes'},
        ),
        migrations.AlterField(
            model_name='class',
            name='friday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='monday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='saturday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='sunday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='thursday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='tuesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='class',
            name='wednesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Closed', 'Closed')], default='Closed', max_length=100, verbose_name='Wednesday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='friday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='monday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='saturday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='sunday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='thursday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='tuesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='privateonlineclass',
            name='wednesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Wednesday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='friday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Friday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='monday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Monday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='saturday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Saturday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='sunday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Sunday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='thursday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Thursday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='tuesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Tuesday'),
        ),
        migrations.AlterField(
            model_name='publiconlineclass',
            name='wednesday',
            field=models.CharField(choices=[('10:00-14:00', '10:00-14:00'), ('14:00-16:00', '14:00-16:00'), ('16:00-18:00', '16:00-18:00'), ('18:00-20:00', '18:00-20:00'), ('20:00-22:00', '20:00-22:00'), ('Offline', 'Offline')], default='Offline', max_length=100, verbose_name='Wednesday'),
        ),
    ]
