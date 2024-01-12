from django.db import models
from datetime import datetime
class Professeurs(models.Model):
    prof_numero = models.CharField(max_length=5, primary_key=True)  # Assuming the 'N°' field is a unique identifier for Professeur
    prof_qualite = models.CharField(max_length=10)  # M, Mme, Mlle, etc.
    prof_nom = models.CharField(max_length=100)
    prof_prenom = models.CharField(max_length=100)
    prof_adresse = models.CharField(max_length=255)
    prof_suite = models.CharField(max_length=100, blank=True)  # Additional address information, optional field
    prof_code_postal = models.CharField(max_length=5)  # French postal codes have 5 digits
    prof_ville = models.CharField(max_length=100)
    prof_tel_ecole = models.CharField(max_length=20, blank=True)
    prof_tel_domicile = models.CharField(max_length=20, blank=True)  # Assuming this field can be optional
    prof_date_embauche = models.DateField()  # Dates should use the DateField type
    prof_date_depart = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Professeurs"
    def __str__(self):
        return f"{self.prof_nom} {self.prof_prenom}"
class Competences(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField()

# #
class TypeDeStages(models.Model):
    code_type = models.IntegerField(primary_key=True)  # Assuming that code_type is unique and can be used as a primary key.
    nb_semaines = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.code_type}"
#
#
class Acquerir(models.Model):
    code = models.ForeignKey(Competences,on_delete=models.CASCADE, null=True)
    code_type = models.ForeignKey(TypeDeStages,on_delete=models.CASCADE, null=True)
    niv_exigence = models.IntegerField()

class Tuteurs(models.Model):
    i = 0
    tuteur_numero = models.CharField(max_length=10, primary_key=True)
    tuteur_entreprise = models.CharField(max_length=20)
    tuteur_qualite = models.CharField(max_length=10)
    tuteur_nom = models.CharField(max_length=100)
    tuteur_prenom = models.CharField(max_length=100)
    tuteur_telephone = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "Tuteurs"

    def __str__(self):
        return f"{self.tuteur_nom} {self.tuteur_prenom}"

#
#
class Annees(models.Model):
    annee = models.IntegerField(primary_key=True)
    def __str__(self):
        return f"{self.annee}"

#
class Entreprises(models.Model):

    n_siret = models.CharField(max_length=14, unique=True,primary_key=True,default="")  # SIRET numbers are 14 digits long
    forme_juridique = models.CharField(max_length=10)
    raison_sociale = models.CharField(max_length=200)
    entreprise_adresse = models.CharField(max_length=255)
    entreprise_suite = models.CharField(max_length=100, blank=True)  # optional
    entreprise_code_postal = models.CharField(max_length=5)  # French postal codes are 5 digits
    entreprise_ville = models.CharField(max_length=100)
    entreprise_telephone = models.CharField(max_length=20)
    entreprise_fax = models.CharField(max_length=20)
    entreprise_contact = models.CharField(max_length=100)
    entreprise_tel_contact = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.n_siret}"

    class Meta:
        verbose_name_plural = "Entreprises"
#
# class inscriptions(models.Model):

#     qualite = models.CharField(max_length=4)
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     adress = models.CharField(max_length=100)
#     suite = models.CharField(blank=True, max_length=100)
#     code_postal = models.CharField(max_length=100)
#     ville = models.CharField(max_length=100)
#     sexe = models.CharField(max_length=1)
#     date_naissance = models.DateField(null=True)
#     telephone = models.CharField(max_length=100)
#     admis = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.nom} {self.prenom}"

class effectuer(models.Model):
    code_type = models.ForeignKey(TypeDeStages,on_delete=models.CASCADE, null=True)
    annee = models.ForeignKey(Annees,on_delete=models.CASCADE, null=True)
    debut = models.DateField()
    fin = models.DateField()
     # def __str__(self):
     #     return f"de {datetime(self.debut).strftime('%Y-%m-%d')} à "
#
class Associer(models.Model):
    n_tuteur = models.ForeignKey(Tuteurs,on_delete=models.CASCADE,default="")
    n_siret = models.ForeignKey(Entreprises,on_delete=models.CASCADE,default="")
class Promos(models.Model):
    annee = models.CharField(max_length=4, primary_key=True)  # Assuming annee is a year format YYYY
    nb_inscrit = models.IntegerField(blank=True, default=0)
    nb_recus = models.IntegerField(blank=True, default=0)
    prof_num = models.ForeignKey(Professeurs, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.annee}"

    class Meta:
        verbose_name_plural = "Promos"


class Etudiants(models.Model):

    id = models.CharField(primary_key=True, max_length=30)
    id_user = models.CharField(max_length=100,unique=True,default="")
    etudiant_n_promo = models.CharField(max_length=20) # id_inscription
    etudiant_promo = models.ForeignKey(Promos, on_delete=models.CASCADE) # promo
    etudiant_qualite = models.CharField(max_length=10)  # e.g., Mr, Mme, etc.
    etudiant_nom = models.CharField(max_length=100)
    etudiant_prenom = models.CharField(max_length=100)
    etudiant_adresse = models.CharField(max_length=255)
    etudiant_suite = models.CharField(max_length=255, blank=True)
    etudiant_code_postal = models.CharField(max_length=5)  # French postal codes have 5 digits
    etudiant_ville = models.CharField(max_length=100)
    etudiant_sexe = models.CharField(max_length=1)  # M or F
    etudiant_naissance = models.DateField()  # Assuming a DateField for a date of birth
    etudiant_num_tel = models.CharField(max_length=20)
    etudiant_mention = models.CharField(max_length=50, blank=True)



    def __str__(self):
        return f"{self.etudiant_nom} {self.etudiant_prenom}"
    class Meta:
        verbose_name_plural = "Etudiants"
class Stages(models.Model):
    n_stage = models.CharField(max_length=10, primary_key=True,default="")
    promo = models.ForeignKey(Promos, on_delete=models.CASCADE, default="")
    compte_rendu = models.TextField(blank=True)  # Assuming this can be an optional field
    tuteur = models.ForeignKey(Tuteurs, on_delete=models.CASCADE)
    code_type = models.ForeignKey(TypeDeStages, on_delete=models.CASCADE)
    prof_num = models.ForeignKey(Professeurs, on_delete=models.CASCADE)
    siret = models.ForeignKey(Entreprises, on_delete=models.CASCADE, default="")
    etudiant_promo = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    annee = models.ForeignKey(Annees, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    fiche_évaluation = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.etudiant_promo } {self.code_type}"
    class Meta:
        verbose_name_plural = "Stages"