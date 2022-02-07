from django.contrib import admin
from .models import Location, Client, Velo
# Register your models here.
admin.site.register(Velo)
admin.site.register(Client)
admin.site.register(Location)
