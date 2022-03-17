
from django.contrib import admin
from django.urls import path, include
from django_otp.admin import OTPAdminSite

class OTPAdmin(OTPAdminSite):
    pass
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

admin_site = OTPAdmin(name= 'OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('admin/', admin_site.urls),
    path('',include('accueil.urls')),
    path('location/',include('location.urls')),
    path('client/',include('client.urls')),
    path('compte/',include('compte.urls')),
    path('stock_velos/',include('stock_velos.urls')),
    path('stock_pieces_velos/',include('stock_pieces_velos.urls')),
    path('stock_locaux/',include('stock_locaux.urls')),
    path('réparations/', include('reparation.urls')),
    path('statistique/', include('statistique.urls')),

]
