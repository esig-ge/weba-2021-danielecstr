import time

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm
from dateutil.relativedelta import relativedelta
import datetime


def locationAcceuil(request):
    return render(request, 'locationAcceuil.html')
def locationAcceuil2(request):
    return render(request, 'locationAcceuil2.html')

def listelocation(request):
    locationAll = Location.objects.all()
    data =  {}
    locations = []
    for loc in locationAll:
        locations.append(loc.serialize())
    data['locations'] = locations
    return  JsonResponse(data)



def location(request):
    locationAll = Location.objects.all()
    #Liste des locations
    locations = []
    for loc in locationAll:
            locations.append(loc)

    context = {
        'locations' : locations,
    }
    return render(request, 'location.html', context)

def detailsLocation(request, id):
    location = Location.objects.get(loc_num=id)
    messageDescriptionVelo = f"Il n'y a pas de remarque"

    if location.loc_vel_id.vel_remarque != "" :
        messageDescriptionVelo = location.loc_vel_id.vel_remarque

    nbMois = relativedelta(location.loc_date_fin,location.loc_date_debut).months
    prix = 50 + ((nbMois-3) * 5)
    montantTotal = prix + 150

    date = datetime.date.today()

    context = {
        'locationvelo' : location,
        'messageDescriptionVelo' : messageDescriptionVelo,
        'date': date,
        'prix' : prix,
        'montantTotal' : montantTotal
    }
    return render(request, 'detailsLocation.html', context)



def nouvelleLocation(request):
    formLocation = LocationForm()
    messageErreur = ""
    if request.method=='POST':
        formLocation = LocationForm(request.POST)
        if formLocation.is_valid():
            dureeMin = formLocation.cleaned_data.get('loc_date_debut') + relativedelta(months=3)
            dureeMax = formLocation.cleaned_data.get('loc_date_debut') + relativedelta(months=12)
            if formLocation.cleaned_data.get('loc_date_fin') > dureeMin and formLocation.cleaned_data.get('loc_date_fin') < dureeMax:
                formLocation.save()
                loc = Location.objects.get(loc_num= formLocation.cleaned_data.get('loc_num'))
                nbMois = relativedelta(formLocation.cleaned_data.get('loc_date_fin'), formLocation.cleaned_data.get('loc_date_debut')).months
                prix = 50 + ((nbMois - 3) * 5)
                montantTotal = prix + 150
                loc.montant = montantTotal
                loc.save()
                return redirect('/location')
            elif formLocation.cleaned_data.get('loc_date_debut') < datetime.date.today():
                messageErreur = "La date de debut ne peut pas être dans le passé."
            elif formLocation.cleaned_data.get('loc_date_fin') < dureeMin:
                messageErreur = "La location doit être au minium de 3 mois."
            elif formLocation.cleaned_data.get('loc_date_fin') > dureeMax:
                messageErreur = "La location doit être au maximum d'un ans."
    context = {
        'formLocation' : formLocation,
        'messageErreur' : messageErreur,
    }
    return render(request, 'nouvelleLocation.html', context)