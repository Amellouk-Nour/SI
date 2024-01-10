from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random
import string


existing_sirets = set()

def generate_unique_siret(existing_sirets):
    """Génère un numéro de SIRET aléatoire et unique."""
    while True:
        siren = str(random.randint(100000000, 999999999))
        nic = str(random.randint(0, 99999)).zfill(5)
        siret = siren + nic

        if siret not in existing_sirets:
            return siret

def generate_unique_id():
    """
    Generates a unique alphanumeric ID with a pattern similar to the one in the given list.
    The pattern is two digits followed by a letter, followed by two digits.
    """
    # Generating a random ID following the pattern
    id = f"{random.randint(10, 99)}{random.choice(string.ascii_uppercase)}{random.randint(10, 99)}"
    return id



# Exemple d'utilisation
 # Ensemble des SIRETs déjà générés
# for _ in range(10):  # Générer 10 numéros de SIRET
#     siret = generate_unique_siret(existing_sirets)
#     existing_sirets.add(siret)
#     print(siret)
# Create your views here.

def createstage(request):
    return render(request, 'stageform/infostage.html')

def statusstage(request):
    return render(request, 'stageform/fiche.html')

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def stage_form_postuler(request):
    if request.method == 'POST':
        forme_juridique = request.POST.get('forme_juridique')
        raison_sociale = request.POST.get('raison_sociale')
        entreprise_adresse = request.POST.get('entreprise_adresse')
        entreprise_suite = request.POST.get('entreprise_suite')
        entreprise_code_postal = request.POST.get('entreprise_code_postal')
        entreprise_ville = request.POST.get('entreprise_ville')
        entreprise_telephone = request.POST.get('entreprise_telephone')
        entreprise_fax = request.POST.get('entreprise_fax')
        entreprise_contact = request.POST.get('entreprise_contact')
        entreprise_tel_contact = request.POST.get('entreprise_tel_contact')
        n_siret = generate_unique_siret(existing_sirets)
        existing_sirets.add(n_siret)

        tuteur_numero = generate_unique_id()

        tuteur_qualite = request.POST.get('tuteur_qualite')
        tuteur_nom = request.POST.get('tuteur_nom')
        tuteur_prenom = request.POST.get('tuteur_prenom')
        tuteur_telephone = request.POST.get('tuteur_telephone')

        new_tuteur = Tuteurs.objects.create(tuteur_numero=tuteur_numero, tuteur_entreprise= n_siret, tuteur_qualite = tuteur_qualite, tuteur_nom = tuteur_nom , tuteur_prenom = tuteur_prenom, tuteur_telephone = tuteur_telephone )
        new_entreprise = Entreprises.objects.create(n_siret=n_siret, forme_juridique=forme_juridique, raison_sociale=raison_sociale, entreprise_adresse=entreprise_adresse, entreprise_suite=entreprise_suite, entreprise_code_postal=entreprise_code_postal, entreprise_ville=entreprise_ville, entreprise_telephone=entreprise_telephone, entreprise_fax=entreprise_fax, entreprise_contact=entreprise_contact, entreprise_tel_contact=entreprise_tel_contact)
    else:
        print('sa marche pas')
    return render(request,"stageform/fiche.html")

