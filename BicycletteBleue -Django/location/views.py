"""
Auteur : Daniele Castro
"""

from django.shortcuts import render,redirect
from .models import Location
from .models import Velo
from .models import Client
from .models import Location_Velo
from .forms import LocationForm
from .forms import LocationVeloForm
from .forms import LocationVeloForm2
from .forms import LocationVeloForm22
from .forms import ClientForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dateutil.relativedelta import relativedelta
from .filters import LocationFilter
import datetime

from django.core.mail import send_mail
from django.conf import settings

@staff_member_required
@login_required(login_url='/compte/login')
def location(request):
    locationvelo = Location_Velo.objects.all()
    location_number = locationvelo.count()
    messageNbLocation = f' Total des locations : {location_number} '
    if location_number == 1:
        messageNbLocation = f' Total des locations : une seule location'
    elif location_number == 0:
        messageNbLocation = f' Aucune location'
    date =datetime.date.today()


    #Envoye un mail aux clients qui finissent leurs location dans 10 jours
    listeMail = []
    for loc in locationvelo:
        if loc.mail_envoyer == "False" and loc.ends_within_10_days() and not loc.termine() and not loc.annule():
            loc.mail_envoyer = "True"
            loc.save()
            listeMail.append(loc.lv_loc_id.loc_client.cli_mail)
    messageMail = 'Bonjour, nous vous envoyons ce mail pour vous prévenir que votre location se termine dans 10 jours.' \
                  '\nVeuillez ne pas oublier de rendre votre vélo ou prolonger votre location depuis notre site : http://danielecstr.pythonanywhere.com/.' \
                  "\n\nToute l'équipe Bicyclette Bleue vous souhaite une bonne journée."
    send_mail('La bicycletteBleue', messageMail , settings.EMAIL_HOST_USER, listeMail, fail_silently=False)

    #Liste des locations
    locations = []
    for loc in locationvelo:
        if loc.loc_statut != "En attente" and loc.loc_statut != "Demande de prolongation" and loc.loc_statut != "Demande de diminution":
            locations.append(loc)

    #Filtrer les locations grace aux statuts
    myfilter = LocationFilter(request.GET, queryset=locationvelo)
    locations = myfilter.qs

    context = {
        'messageNbLocation' : messageNbLocation,
        'date' : date,
        'myfilter' : myfilter,
        'locations' : locations,
        'listeMail' : listeMail
    }
    return render(request, 'location/location.html', context)



@staff_member_required
@login_required(login_url='/compte/login')
def locationEnAttente(request):
    locationvelo = Location_Velo.objects.all()
    date =datetime.date.today()
    locationEnAttente = []
    for loc in locationvelo:
        if loc.lv_loc_id.loc_statut == "En attente" or loc.lv_loc_id.loc_statut == "Demande de diminution" or loc.lv_loc_id.loc_statut == "Demande de prolongation":
            locationEnAttente.append(loc)
    location_number = len(locationEnAttente)
    messageNbLocation = f' Total des locations : {location_number} '
    if location_number == 1:
        messageNbLocation = f' Total des locations : une seule location'
    elif location_number == 0:
        messageNbLocation = f' Aucune location en attente'
    context = {
        'messageNbLocation' : messageNbLocation,
        'locationvelo': locationvelo,
        'date' : date,
        'locationEnattente' : locationEnAttente
    }
    return render(request, 'location/locationEnAttente.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def confirmationLocation(request, pk):
    location = Location.objects.get(loc_num=pk)
    locationVelo = Location_Velo.objects.get(loc_num=pk)

    if request.method=='POST':
        if location.loc_statut == "Demande de prolongation":
            messageMail = "Votre demande de prolongation de la location à été accepter"
        elif location.loc_statut == "Demande de diminution":
            messageMail = "Votre demande diminution de location à été accepter"
        else:
            messageMail = "Votre demande de location à bien été acceptée"

        locationVelo.lv_vel_id.vel_statut = "Reservé"
        locationVelo.lv_vel_id.save()
        locationVelo.loc_statut = "En cours"
        locationVelo.save()
        location.loc_statut = "En cours"
        location.save()

        #Permet d'envoyer un mail selon la décision du membre
        send_mail('La bicycletteBleue', messageMail , settings.EMAIL_HOST_USER, [location.loc_client.cli_mail], fail_silently=False)

        return redirect('/location/locationEnAttente')

    context = {
        'itemLocation': location,
        'itemLocationVelo' : locationVelo
    }
    return render(request, 'location/confirmationLocation.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def detailsLocation(request, id):
    locationvelo = Location_Velo.objects.get(loc_num=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"
    if locationvelo.lv_vel_id.vel_remarque != "" :
        messageDescriptionVelo = locationvelo.lv_vel_id.vel_remarque

    nbMois = relativedelta(locationvelo.date_fin,locationvelo.date_debut).months
    prix = 50 + ((nbMois-3) * 5)
    montantTotal = prix + 150

    date =datetime.date.today()

    context = {
        'locationvelo' : locationvelo,
        'messageDescriptionVelo' : messageDescriptionVelo,
        'date': date,
        'prix' : prix,
        'montantTotal' : montantTotal
    }
    return render(request, 'location/detailsLocation.html', context)

@staff_member_required
@login_required(login_url='/compte/login')
def detailsLocationEnAttente(request, id):
    locationvelo = Location_Velo.objects.get(loc_num=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"
    if locationvelo.lv_vel_id.vel_remarque != "" :
        messageDescriptionVelo = locationvelo.lv_vel_id.vel_remarque

    date =datetime.date.today()

    context = {
        'locationvelo' : locationvelo,
        'messageDescriptionVelo' : messageDescriptionVelo,
        'date': date
    }
    return render(request, 'location/detailsLocationEnAttente.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def nouvelleLocation(request):
    formLocationVelo = LocationVeloForm()
    formLocation = LocationForm()
    messageErreur = ""
    if request.method=='POST':
        formLocation=LocationForm(request.POST)
        formLocationVelo = LocationVeloForm(request.POST)
        if formLocation.is_valid() and formLocationVelo.is_valid():
            dureeMin = formLocationVelo.cleaned_data.get('date_debut') + relativedelta(months=3)
            dureeMax = formLocationVelo.cleaned_data.get('date_debut') + relativedelta(months=12)
            if formLocationVelo.cleaned_data.get('date_fin') > dureeMin and formLocationVelo.cleaned_data.get('date_fin') < dureeMax:
                if Location.objects.all().count() == 0:
                    nb = 1
                else:
                    nb = Location.objects.latest('loc_id').loc_num + 1
                loca = Location(loc_statut=formLocation.cleaned_data.get('loc_statut'), loc_client_id=formLocation.cleaned_data.get('loc_client').cli_id, loc_num=nb)
                loca.save()
                nbmax = Location.objects.latest('loc_id').loc_id
                locaVelo = Location_Velo(loc_statut=formLocation.cleaned_data.get('loc_statut'),date_fin=formLocationVelo.cleaned_data.get('date_fin'), date_debut=formLocationVelo.cleaned_data.get('date_debut'),lv_loc_id_id=nbmax, id=nbmax,lv_vel_id_id=formLocationVelo.cleaned_data.get('lv_vel_id').vel_id)
                locaVelo.lv_vel_id.vel_statut= "Reservé"
                locaVelo.lv_vel_id.save()
                locaVelo.save()
                return redirect('/location')

            elif formLocationVelo.cleaned_data.get('date_debut') < datetime.date.today():
                messageErreur = "La date de debut ne peut pas être dans le passé."
            elif formLocationVelo.cleaned_data.get('date_fin') < dureeMin:
                messageErreur = "La location doit être au minium de 3 mois."
            elif formLocationVelo.cleaned_data.get('date_fin') > dureeMax:
                messageErreur = "La location doit être au maximum d'un ans."
    context = {
        'formLocation' : formLocation,
        'formLocationVelo' : formLocationVelo,
        'messageErreur' : messageErreur,
    }
    return render(request, 'location/nouvelleLocation.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def modifierlocation(request, pk):
    location = Location.objects.get(loc_num=pk)
    formLocation=LocationForm(instance=location)
    location2 = Location_Velo.objects.get(loc_num=pk)
    formLocationVelo = LocationVeloForm(instance=location2)

    if request.method=='POST':
        formLocation=LocationForm(request.POST, instance=location)
        formLocationVelo=LocationVeloForm(request.POST, instance=location2)
        if formLocation.is_valid() and formLocationVelo.is_valid():
            formLocation.save()
            formLocationVelo.save()
            return redirect('/location')
    context = {
        'formLocation' : formLocation,
        'formLocationVelo' : formLocationVelo
    }
    return render(request, 'location/nouvelleLocation.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def supprimerLocation(request, pk):
    location = Location.objects.get(loc_num=pk)
    locationVelo = Location_Velo.objects.get(loc_num=pk)
    if request.method=='POST':
        locationVelo.lv_vel_id.vel_statut = "Libre"
        locationVelo.lv_vel_id.save()
        location.delete()
        return redirect('/location')
    context = {
        'itemLocation': location,
        'itemLocationVelo' : locationVelo
    }
    return render(request, 'location/supprimerLocation.html', context)


@staff_member_required
@login_required(login_url='/compte/login')
def refuseLocationEnAttente(request, pk):
    location = Location.objects.get(loc_num=pk)
    locationVelo = Location_Velo.objects.get(loc_num=pk)
    if request.method=='POST':
        if location.loc_statut == "Demande de prolongation":
            messageMail = "Votre demande de prolongation de la location à été refusée"
        elif location.loc_statut == "Demande de diminution":
            messageMail = "Votre demande diminution de location à été refusée"
        else:
            messageMail = "Votre demande de location à bien été refusé"

        send_mail('La bicycletteBleue', messageMail , settings.EMAIL_HOST_USER, [location.loc_client.cli_mail], fail_silently=False)

        if location.loc_statut == "Demande de diminution" or location.loc_statut == "Demande de prolongation":
            location.loc_statut = "En cours"
            locationVelo.loc_statut = "En cours"
            locationVelo.date_fin = location.date_modifier
            location.save()
            locationVelo.save()
            return redirect('/location/locationEnAttente')
        else:
            locationVelo.lv_vel_id.vel_statut = "Libre"
            locationVelo.loc_statut = "Annulé"
            locationVelo.lv_vel_id.save()
            location.loc_statut = "Annulé"
            location.save()
            return redirect('/location/locationEnAttente')
    context = {
        'itemLocation': location,
        'itemLocationVelo' : locationVelo
    }
    return render(request, 'location/refuseLocationEnAttente.html', context)



################################################################################################################
#############################################LA PARTIE CLIENT###################################################
################################################################################################################


@login_required(login_url='/compte/login')
def locationClient(request, pk):
    date =datetime.date.today()
    locations = []
    locationAll = Location_Velo.objects.all()
    for loc in locationAll:
        if pk == str(loc.lv_loc_id.loc_client.cli_id):
            locations.append(loc)
            if loc.date_fin < date:
                loc.loc_statut = "Terminé"
                loc.save()
                loc.lv_loc_id.loc_statut = "Terminé"
                loc.lv_loc_id.save()

    location_number = len(locations)

    messageNbLocation = f'{location_number} locations :'
    if location_number == 1:
        messageNbLocation = f'{location_number} location :'

    context = {
        'location' : location,
        'messageNbLocation' : messageNbLocation,
        'date' : date,
        'locations' : locations
    }

    return render(request, 'location/locationClient.html', context)


@login_required(login_url='/compte/login')
def detailsLocationClient(request, id):
    locationvelo = Location_Velo.objects.get(loc_num=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"
    if locationvelo.lv_vel_id.vel_remarque != "" :
        messageDescriptionVelo = locationvelo.lv_vel_id.vel_remarque

    date =datetime.date.today()


    nbMois = relativedelta(locationvelo.date_fin,locationvelo.date_debut).months
    prix = 50 + ((nbMois-3) * 5)
    montantTotal = prix + 150
    context = {
        'locationvelo' : locationvelo,
        'messageDescriptionVelo' : messageDescriptionVelo,
        'date': date,
        'prix' : prix,
        'montantTotal': montantTotal,
    }
    return render(request, 'location/detailsLocationClient.html', context)


@login_required(login_url='/compte/login')
def supprimerLocationClient(request, pk):
    location = Location.objects.get(loc_num=pk)
    pk2 = location.loc_num
    locationVelo = Location_Velo.objects.get(loc_num=pk2)
    if request.method=='POST':
        locationVelo.loc_statut = "Annulé"
        locationVelo.save()
        location.loc_statut = "Annulé"
        location.save()
        locationVelo.lv_vel_id.vel_statut = "Libre"
        locationVelo.lv_vel_id.save()
        cli = request.user.id
        return redirect('/location/locationClient/' + str(cli))
    context = {
        'itemLocation': location,
        'itemLocationVelo': locationVelo,
    }
    return render(request, 'location/supprimerLocationClient.html', context)


@login_required(login_url='/compte/login')
def modifierlocationClient(request, pk):
    location = Location_Velo.objects.get(loc_num=pk)
    vieille_date = location.date_fin
    formLocationVelo = LocationVeloForm22(instance=location)
    messageErreur = ""
    if request.method=='POST':
        formLocationVelo =LocationVeloForm22(request.POST, instance=location)
        if formLocationVelo.is_valid():
            dureeMin = location.date_debut +  relativedelta(months=3)
            dureeMax = location.date_debut +  relativedelta(months=12)
            if formLocationVelo.cleaned_data.get('date_fin') < location.date_debut:
                messageErreur = "La date de fin ne peut pas être dans le passé ou avant la date de debut."
            elif formLocationVelo.cleaned_data.get('date_fin') < dureeMin:
                    messageErreur = "La location doit être au minium de 3 mois."
            elif formLocationVelo.cleaned_data.get('date_fin') > dureeMax:
                messageErreur = "La location doit être au maximum d'un ans."
            elif vieille_date == formLocationVelo.cleaned_data.get('date_fin'):
                messageErreur = "Veuillez inserer une date de fin différente de celle de la location"
            else:
                location = Location.objects.get(loc_num=pk)
                location.date_modifier = vieille_date
                if vieille_date > formLocationVelo.cleaned_data.get('date_fin'):
                    location.loc_statut = "Demande de diminution"
                elif vieille_date < formLocationVelo.cleaned_data.get('date_fin'):
                    location.loc_statut = "Demande de prolongation"
                location.save()
                formLocationVelo.save()
                return redirect('/location/locationClient/' + str(request.user.id))
    context = {
        'formLocationVelo' : formLocationVelo,
        'location' : location,
        'messageErreur' : messageErreur,
        'vieille_date' : vieille_date
    }
    return render(request, 'location/modificationLocationClient.html', context)




@login_required(login_url='/compte/login')
def choixVeloClient(request):
    veloDispo = []
    velos_objets = Velo.objects.all()
    messageAttention = ""
    locationAll = Location_Velo.objects.all()
    nbEnCours = 0
    for loc in locationAll:
        if request.user.id == loc.lv_loc_id.loc_client.cli_id:
            if loc.lv_loc_id.loc_statut == "En cours":
                nbEnCours += 1
    if nbEnCours == 1:
        messageAttention = "Attention vous avez deja une location en cours !"
    elif nbEnCours > 0:
        messageAttention = "Attention vous avez deja " + str(nbEnCours) + " location en cours !"

    for velo in velos_objets:
        if velo.vel_statut == "Libre":
            veloDispo.append(velo)
    context = {
        'velosObjets': velos_objets,
        'veloDispo' : veloDispo,
        'messageAttention' : messageAttention
    }

    return render(request, 'location/choixVeloClient.html', context)

def donneeLocationClient(request, pk):
    messageErreur = ""
    client = Client.objects.get(cli_id=request.user.id)
    velo = Velo.objects.get(vel_num=pk)
    clientForm = ClientForm(instance=client)
    if request.method == 'POST':
        clientForm = ClientForm(request.POST, instance=client)
        if clientForm.is_valid():
            if clientForm.cleaned_data.get('cli_date_naissance') + relativedelta(months=216) < datetime.date.today():
                clientForm.save()
                return redirect('/location/finaliserLocationClient/' + pk)
            else:
                messageErreur = "Vous devez avoir au moins 18 ans pour louer un vélo."
    context = {
        'client' : client,
        'velo' : velo,
        'clientForm' :clientForm,
        'messageErreur': messageErreur
    }

    return render(request, 'location/donneeLocationClient.html', context)

def finaliserLocationClient(request, pk):
    messageErreur = ""
    client = Client.objects.get(cli_id=request.user.id)
    velo = Velo.objects.get(vel_num=pk)
    formLocationVelo = LocationVeloForm2()
    if request.method == 'POST':
        formLocationVelo = LocationVeloForm2(request.POST)
        if formLocationVelo.is_valid():
            dureeMin = formLocationVelo.cleaned_data.get('date_debut') +  relativedelta(months=3)
            dureeMax = formLocationVelo.cleaned_data.get('date_debut') +  relativedelta(months=12)
            if formLocationVelo.cleaned_data.get('date_debut') < datetime.date.today():
                messageErreur = "La date de debut ne peut pas être dans le passé."
            elif formLocationVelo.cleaned_data.get('date_fin') < dureeMin:
                messageErreur = "La location doit être au minium de 3 mois."
            elif formLocationVelo.cleaned_data.get('date_fin') > dureeMax:
                messageErreur = "La location doit être au maximum d'un ans."
            else:
                if Location.objects.all().count() == 0:
                    nb = 1
                else:
                    nb = Location.objects.latest('loc_id').loc_num + 1
                loca = Location(loc_statut="En attente", loc_client_id=client.cli_id, loc_num=nb)
                loca.save()
                nbmax = Location.objects.latest('loc_id').loc_id
                locaVelo = Location_Velo(loc_statut="En attente", date_fin=formLocationVelo.cleaned_data.get('date_fin'),
                                     date_debut=formLocationVelo.cleaned_data.get('date_debut'), lv_loc_id_id=nbmax,
                                     id=nbmax, lv_vel_id_id=velo.vel_id, loc_num=nb)
                locaVelo.save()
                velo.vel_statut = "Reservé"
                velo.save()
                return redirect('/location/locationClient/' + str(client.cli_id))

    context = {
        'client' : client,
        'velo' : velo,
        'formLocationVelo': formLocationVelo,
        'messageErreur' : messageErreur
    }

    return render(request, 'location/finaliserLocationClient.html', context)

