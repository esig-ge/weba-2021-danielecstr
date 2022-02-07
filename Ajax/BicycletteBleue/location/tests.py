import django.test
from django.test import TestCase
from django.urls import reverse

from .models import Location , Velo, Client
from datetime import datetime
class locationTest(TestCase):
    def setUp(self):
        self.v = Velo.objects.create(vel_id=1, vel_num_cadre=1, vel_nom="Velo1", vel_marque="Speeed",
                                     vel_couleur="Rouge", vel_type="VTT", vel_statut="Libre", vel_etat="Bon etat",
                                     vel_remarque="", vel_num=1)
        self.c = Client.objects.create(cli_id=1, cli_nom="Castro", cli_prenom="Daniele", cli_adresseposte="Avenue ..",
                                       cli_date_naissance="1997-02-11", cli_mail="Dani@eduge.ch", cli_tel=0000000000,
                                       cli_membre="Non", cli_num=1)
        self.date_debut = '2020-02-11'
        self.date_fin = '2020-06-11'

    def test_si_location_a_montant(self):
        self.assertEqual(hasattr(Location, 'montant'), True)




    def test_si_nouvelleLoc_a_bon_montant(self):
        d1 = datetime.strptime(self.date_debut, "%Y-%m-%d")
        d2 = datetime.strptime(self.date_fin, "%Y-%m-%d")
        nbMois = round(abs((d2 - d1).days) / 30)
        prix = 50 + ((nbMois - 3) * 5)
        montantTotal = prix + 150
        client = django.test.Client()
        data = {'loc_vel_id': '1', 'loc_id': 1, 'loc_date_debut': self.date_debut,
                'loc_date_fin': self.date_fin,
                'loc_cli_id': '1',
                'loc_statut': 'Terminé',
                'loc_num': 1}
        response = client.post(reverse('location:nouvelleLocation'), data)
        self.assertEqual(Location.objects.get(loc_num =1).montant, montantTotal)
