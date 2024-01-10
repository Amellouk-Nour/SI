from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import inscriptions, Etudiants
from datetime import datetime

@receiver(post_save, sender=inscriptions)
def create_etudiant(sender, instance, created, **kwargs):
    if instance.admis:
        Etudiants.objects.create(
            etudiant_promo=datetime.now().year
            etudiant_qualite=instance.qualite,
            etudiant_nom=instance.nom,
            etudiant_prenom=instance.prenom,
            etudiant_adresse=instance.adresse,
            etudiant_suite=instance.suite,
            etudiant_code_postal=instance.code_postal,
            etudiant_ville=instance.ville,
            etudiant_sexe=instance.sexe,
            etudiant_naissance=instance.date_naissance,
            etudiant_num_tel=instance.telephone,

        )