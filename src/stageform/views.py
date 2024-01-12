from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import random
import string
from datetime import datetime, timedelta
from django.utils import timezone
import pdfkit
from django.template.loader import render_to_string
import os
from .forms import UploadFileForm
def generate_pdf_view(request):
    user_id = request.user.id
    etudiant_id = Etudiants.objects.get(id_user=user_id).id
    if Stages.objects.filter(etudiant_promo_id=etudiant_id):
        stage = Stages.objects.filter(etudiant_promo_id=etudiant_id).order_by('code_type_id').last()
        nom_user= Etudiants.objects.get(id_user=user_id).etudiant_nom
        prenom_user= Etudiants.objects.get(id_user=user_id).etudiant_prenom
        type_stage_user= stage.code_type_id
        tuteur_user= f"{Tuteurs.objects.get(tuteur_numero=stage.tuteur_id).tuteur_nom} {Tuteurs.objects.get(tuteur_numero=stage.tuteur_id).tuteur_prenom}"
        entreprise_user= stage.siret_id

        # nom_user='frde'
        # prenom_user='trfe'
        # type_stage_user='trfe'
        # tuteur_user='ytvfdd'
        # entreprise_user='ytvfdd'

        context = {
            'nom_user': nom_user,
            'prenom_user': prenom_user,
            'type_stage_user': type_stage_user,
            'tuteur_user': tuteur_user,
            'entreprise_user': entreprise_user
        }

        output_text = render_to_string('stageform/pdfstage.html', context)


        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        pdf = pdfkit.from_string(output_text, False, configuration=config)

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="generated_pdf.pdf"'

        return response




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

    user_id = request.user.id
    etudiant_id = Etudiants.objects.get(id_user=user_id).id
    if Stages.objects.filter(etudiant_promo_id=etudiant_id):
        last_stage = Stages.objects.filter(etudiant_promo_id=etudiant_id).order_by('code_type_id').last()

        return render(request, 'stageform/fiche.html', context={"stage" : last_stage})

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
        print(Promos.objects.get(annee=Etudiants.objects.get(id_user=request.user.id).etudiant_promo_id).prof_num_id)
        prof_annee= Professeurs.objects.get(prof_numero=Promos.objects.get(annee=Etudiants.objects.get(id_user=request.user.id).etudiant_promo_id).prof_num_id)
        promo_stage= Promos.objects.get(annee=Etudiants.objects.get(id_user=request.user.id).etudiant_promo_id)

        # STAGE

        new_effectuer, cree = effectuer.objects.get_or_create(code_type=TypeDeStage, annee=AnneeStage, debut=date_debut, fin=date_fin)
        new_tuteur = Tuteurs.objects.create(tuteur_numero=tuteur_numero, tuteur_entreprise= n_siret, tuteur_qualite = tuteur_qualite, tuteur_nom = tuteur_nom , tuteur_prenom = tuteur_prenom, tuteur_telephone = tuteur_telephone )
        new_entreprise = Entreprises.objects.create(n_siret=n_siret, forme_juridique=forme_juridique, raison_sociale=raison_sociale, entreprise_adresse=entreprise_adresse, entreprise_suite=entreprise_suite, entreprise_code_postal=entreprise_code_postal, entreprise_ville=entreprise_ville, entreprise_telephone=entreprise_telephone, entreprise_fax=entreprise_fax, entreprise_contact=entreprise_contact, entreprise_tel_contact=entreprise_tel_contact)
        new_stage = Stages.objects.create(n_stage=generate_unique_id(), compte_rendu="",
                                          tuteur=new_tuteur, code_type=TypeDeStage, prof_num=prof_annee, siret=new_entreprise, etudiant_promo=Etudiants.objects.get(id_user=request.user.id),annee=Annees.objects.get(annee=str(timezone.now().year)), promo=promo_stage, status="En attente")
    return render(request,"stageform/fiche.html", context={"stage" : new_stage})



def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['fileToUpload']

            if not file.name.endswith('.pdf'):
                return HttpResponse("Erreur : Le fichier n'est pas un PDF")

            custom_upload_dir = 'C:/$Winkernel/formation python/SI_BD/src/stageform/media/uploads'  # Base directory for uploads
            save_path = os.path.join(custom_upload_dir, file.name)

            # Ensure directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            # Save the uploaded file
            with open(save_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Update the stage with the file path
            user_id = request.user.id
            etudiant_id = Etudiants.objects.get(id_user=user_id).id
            stage = Stages.objects.filter(etudiant_promo_id=etudiant_id).order_by('code_type_id').last()
            print(type(file))
            stage.fiche_évaluation = os.path.join('uploads', file.name)
            stage.save()

            return HttpResponse("Sauvegarde du fichier réussie")
        else:
            return HttpResponse("Erreur dans le formulaire")
    else:
        form = UploadFileForm()
        return render(request, "stageform/fiche.html", {'form': form})
