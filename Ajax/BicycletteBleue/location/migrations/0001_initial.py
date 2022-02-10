# Generated by Django 3.2.11 on 2022-01-25 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('cli_id', models.AutoField(primary_key=True, serialize=False)),
                ('cli_nom', models.CharField(max_length=100)),
                ('cli_prenom', models.CharField(max_length=100)),
                ('cli_adresseposte', models.CharField(max_length=100)),
                ('cli_date_naissance', models.DateField()),
                ('cli_mail', models.CharField(max_length=100)),
                ('cli_tel', models.CharField(max_length=100)),
                ('cli_membre', models.CharField(max_length=100)),
                ('cli_date_debut', models.DateField()),
                ('cli_date_fin', models.DateField()),
                ('cli_num', models.IntegerField()),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Velo',
            fields=[
                ('vel_id', models.AutoField(primary_key=True, serialize=False)),
                ('vel_num_cadre', models.IntegerField()),
                ('vel_nom', models.CharField(max_length=100)),
                ('vel_marque', models.CharField(max_length=100)),
                ('vel_couleur', models.CharField(max_length=100)),
                ('vel_type', models.CharField(max_length=100)),
                ('vel_photo', models.CharField(max_length=100)),
                ('vel_statut', models.CharField(max_length=100)),
                ('vel_etat', models.CharField(max_length=100)),
                ('vel_remarque', models.CharField(max_length=100)),
                ('vel_num', models.IntegerField()),
            ],
            options={
                'db_table': 'Velo',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('loc_id', models.AutoField(primary_key=True, serialize=False)),
                ('loc_date_debut', models.DateField()),
                ('loc_date_fin', models.DateField()),
                ('loc_statut', models.CharField(blank=True, choices=[('En cours', 'En cours'), ('Annulé', 'Annulé'), ('Terminé', 'Terminé')], db_column='LOC_STATUT', default='En cours', max_length=30, null=True)),
                ('loc_num', models.IntegerField(db_column='LOC_NUM')),
                ('loc_cli_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.client')),
                ('loc_vel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.velo')),
            ],
            options={
                'db_table': 'Location_Velo',
            },
        ),
    ]