from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import inscriptions
from stageform.models import Etudiants, Promos
from django.utils import timezone

@receiver(post_save, sender=inscriptions)
def create_student_record(sender, instance, created, **kwargs):
    if instance.admis:
        etudiant, cree = Etudiants.objects.get_or_create(
            id=str(instance.id)+" "+str(timezone.now().year+3),
            id_user = instance.id_user,# Supposons que l'ID de l'inscription est utilisé comme ID étudiant
            etudiant_n_promo=instance.id,
            etudiant_promo= Promos.objects.get(annee=str(timezone.now().year+3)),
            etudiant_qualite=instance.qualite,
            etudiant_nom=instance.nom,
            etudiant_prenom=instance.prenom,
            etudiant_adresse=instance.adress,
            etudiant_suite=instance.suite,
            etudiant_code_postal=instance.code_postal,
            etudiant_ville=instance.ville,
            etudiant_sexe=instance.sexe,
            etudiant_naissance=instance.date_naissance,
            etudiant_num_tel=instance.telephone,
            etudiant_mention=''
        )
        if cree :
            print(f"Un nouvel étudiant a été créé pour l'inscription {instance.id}")
        else :
            print("etidiant déjaz present")

@receiver(post_save, sender=inscriptions)
def updatepromo(sender, instance, created, **kwargs):
    if created:
        promoact=Promos.objects.get(annee=str(timezone.now().year+3))
        nb_inscrit = inscriptions.objects.count()
        # nb_etudiant = Etudiants.objects.count()

        promoact.nb_inscrit = nb_inscrit
        # promoact.nb_recus = nb_etudiant
        promoact.save()

@receiver(post_save, sender=Etudiants)
def updatepromo2(sender, instance, created, **kwargs):
    if created:
        promoact=Promos.objects.get(annee=str(timezone.now().year+3))
        # nb_inscrit = inscriptions.objects.count()
        nb_etudiant = Etudiants.objects.count()

        # promoact.nb_inscrit = nb_inscrit
        promoact.nb_recus = nb_etudiant
        promoact.save()