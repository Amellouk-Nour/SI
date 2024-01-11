from django.contrib import admin
from .models import *
from django import forms
# Register your models here.
class entrepriseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entreprises, entrepriseAdmin)

class tuteurAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tuteurs, tuteurAdmin)

admin.site.register(effectuer)
admin.site.register(Promos)
admin.site.register(Etudiants)
admin.site.register(Professeurs)
class StageAdminForm(forms.ModelForm):
    # Définissez un champ ChoiceField pour le champ 'status' avec les options souhaitées
    STATUS_CHOICES = [
        ('En attente', 'En attente'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model = Stages
        fields = '__all__'

class StageAdmin(admin.ModelAdmin):
    form = StageAdminForm  # Utilisez le formulaire personnalisé

admin.site.register(Stages, StageAdmin)