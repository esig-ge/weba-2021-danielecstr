# Generated by Django 3.2.11 on 2022-01-26 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_alter_location_montant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='montant',
            field=models.IntegerField(default=200, null=True),
        ),
    ]
