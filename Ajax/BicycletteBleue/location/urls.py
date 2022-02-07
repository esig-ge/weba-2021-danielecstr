"""
Auteur : Daniele Castro
"""

from django.urls import path, include
from . import views

app_name = 'location'

urlpatterns = [
    path('', views.locationAcceuil2, name='index2'),
    path('location/',views.location, name='location'),
    path('listelocation/', views.listelocation, name='listelocation'),
    path('location/<int:id>/', views.detailsLocation, name='detailsLocation'),
    path('nouvelleLocation/', views.nouvelleLocation, name='nouvelleLocation'),
]
