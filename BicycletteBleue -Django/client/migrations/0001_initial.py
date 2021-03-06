# Generated by Django 4.0 on 2021-12-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cli_id', models.AutoField(db_column='CLI_ID', primary_key=True, serialize=False)),
                ('cli_nom', models.CharField(db_column='CLI_NOM', max_length=100, null=True)),
                ('cli_prenom', models.CharField(db_column='CLI_PRENOM', max_length=100, null=True)),
                ('cli_adresseposte', models.CharField(db_column='CLI_ADRESSEPOSTE', max_length=100, null=True)),
                ('cli_date_naissance', models.DateField()),
                ('cli_mail', models.CharField(db_column='CLI_MAIL', max_length=100, null=True)),
                ('cli_tel', models.CharField(db_column='CLI_TEl', max_length=100, null=True)),
                ('cli_membre', models.CharField(db_column='CLI_MEMBRE', max_length=100, null=True)),
                ('cli_date_debut', models.DateField(blank=True)),
                ('cli_date_fin', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'Client',
                'managed': False,
            },
        ),
    ]
