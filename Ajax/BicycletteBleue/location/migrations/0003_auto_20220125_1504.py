# Generated by Django 3.2.11 on 2022-01-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_location_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='cli_date_debut',
        ),
        migrations.RemoveField(
            model_name='client',
            name='cli_date_fin',
        ),
        migrations.RemoveField(
            model_name='velo',
            name='vel_photo',
        ),
        migrations.AlterField(
            model_name='velo',
            name='vel_remarque',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
