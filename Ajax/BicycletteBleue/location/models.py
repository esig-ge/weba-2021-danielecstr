from django.db import models
from datetime import date


class Client(models.Model):
    cli_id = models.AutoField(primary_key=True)
    cli_nom = models.CharField(max_length=100)
    cli_prenom = models.CharField(max_length=100)
    cli_adresseposte = models.CharField(max_length=100)
    cli_date_naissance = models.DateField()
    cli_mail = models.CharField(max_length=100)
    cli_tel = models.CharField(max_length=100)
    cli_membre = models.CharField( max_length=100)
    cli_num = models.IntegerField()
    def serialize(self):
        cli = {
            "cli_id" : self.cli_id,
            "cli_nom": self.cli_nom,
            "cli_prenom": self.cli_prenom,
            "cli_adresseposte": self.cli_adresseposte,
            "cli_date_naissance": self.cli_date_naissance,
            "cli_mail": self.cli_mail,
            "cli_tel": self.cli_tel,
            "cli_membre": self.cli_membre,
            "cli_num": self.cli_num,
        }
        return cli
    def __str__(self):
        return self.cli_nom  + " " + self.cli_prenom + " (" + str(self.cli_date_naissance) + ")"
    class Meta:
        db_table = 'Client'




class Velo(models.Model):
    vel_id = models.AutoField( primary_key = True)
    vel_num_cadre = models.IntegerField()
    vel_nom = models.CharField(max_length=100)
    vel_marque = models.CharField(max_length=100)
    vel_couleur = models.CharField(max_length=100)
    vel_type = models.CharField(max_length=100)
    vel_statut = models.CharField(max_length=100)
    vel_etat = models.CharField(max_length=100)
    vel_remarque = models.CharField(max_length=100, blank=True)
    vel_num = models.IntegerField()
    def __str__(self):
        return self.vel_nom

    class Meta:
        db_table = 'Velo'



class Location(models.Model):
    STAUT_CHOICES = [
        ('En cours', 'En cours'),
        ('Annulé', 'Annulé'),
        ('Terminé', 'Terminé'), ]
    loc_id = models.AutoField(primary_key = True)
    loc_date_debut = models.DateField()
    loc_date_fin   = models.DateField()
    loc_vel_id = models.ForeignKey(Velo, on_delete=models.CASCADE)
    loc_cli_id = models.ForeignKey(Client, on_delete=models.CASCADE)  #Field name made lowercase.
    loc_statut = models.CharField(blank=True, null=True, max_length=30,choices=STAUT_CHOICES, default='En cours')  # Field name made lowercase.
    loc_num = models.IntegerField(blank=False)
    montant = models.IntegerField(blank=False, null=True, default=0)
    def serialize(self):
        location = {
            "loc_id" : self.loc_id,
            "loc_date_debut": self.loc_date_debut,
            "loc_date_fin": self.loc_date_fin,
            "loc_vel_id": self.loc_vel_id.vel_nom,
            "loc_cli_id": self.loc_cli_id.cli_nom + ' ' + self.loc_cli_id.cli_prenom,
            "loc_statut": self.loc_statut,
            "loc_num": self.loc_num,
            "montant": self.montant,
        }
        return location
    def ends_within_10_days(self):
        return (self.loc_date_fin - date.today()).days < 11
    def termine(self):
        return (date.today() - self.loc_date_fin).days >= 0
    def annule(self):
        return self.loc_statut == "Annulé"
    class Meta:
        db_table = 'Location'

