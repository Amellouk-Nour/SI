from django.contrib import admin

# Register your models here.
from . models import inscriptions

class inscriptionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom']

admin.site.register(inscriptions)