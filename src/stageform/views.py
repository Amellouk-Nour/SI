from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random
import string
from datetime import datetime, timedelta

existing_sirets = set()

def ajouter_semaines(date_str, nb_semaines):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    nouvelle_date = date_obj + timedelta(weeks=nb_semaines)
    return nouvelle_date.strftime('%Y-%m-%d')

def generate_unique_siret(existing_sirets):
    """Génère un numéro de SIRET aléatoire et unique."""
    while True:
        # Generate a random 9-digit SIREN number
        siren = str(random.randint(1, 999999999)).zfill(9)
        # Generate a random 5-digit NIC number
        nic = str(random.randint(0, 99999)).zfill(5)
        # Concatenate SIREN and NIC to form a SIRET number
        siret = siren + nic

        # Check if generated SIRET is unique
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

        date_debut = request.POST.get('date_debut')
        internship_type = request.POST.get('internship_type')
        nb_semaines = TypeDeStages.objects.get(code_type=internship_type).nb_semaines
        date_fin = ajouter_semaines(date_debut, nb_semaines)

        date_debut_obj = datetime.strptime(date_debut, '%Y-%m-%d')
        annee = int(date_debut_obj.year)



        TypeDeStage = TypeDeStages.objects.get(code_type=internship_type)
        AnneeStage = Annees.objects.get(annee=annee)

        # STAGE
        # n_stage = f()

        new_effectuer, cree = effectuer.objects.get_or_create(code_type=TypeDeStage, annee=AnneeStage, debut=date_debut, fin=date_fin)
        new_tuteur = Tuteurs.objects.create(tuteur_numero=tuteur_numero, tuteur_entreprise= n_siret, tuteur_qualite = tuteur_qualite, tuteur_nom = tuteur_nom , tuteur_prenom = tuteur_prenom, tuteur_telephone = tuteur_telephone )
        new_entreprise = Entreprises.objects.create(n_siret=n_siret, forme_juridique=forme_juridique, raison_sociale=raison_sociale, entreprise_adresse=entreprise_adresse, entreprise_suite=entreprise_suite, entreprise_code_postal=entreprise_code_postal, entreprise_ville=entreprise_ville, entreprise_telephone=entreprise_telephone, entreprise_fax=entreprise_fax, entreprise_contact=entreprise_contact, entreprise_tel_contact=entreprise_tel_contact)

    return render(request,"stageform/fiche.html")

