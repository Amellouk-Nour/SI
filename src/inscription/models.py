from django.db import models

class Professeurs(models.Model):
    prof_numero = models.CharField(max_length=5, primary_key=True)  # Assuming the 'N°' field is a unique identifier for Professeur
    prof_qualite = models.CharField(max_length=10)  # M, Mme, Mlle, etc.
    prof_nom = models.CharField(max_length=100)
    prof_prenom = models.CharField(max_length=100)
    prof_adresse = models.CharField(max_length=255)
    prof_suite = models.CharField(max_length=100, blank=True)  # Additional address information, optional field
    prof_code_postal = models.CharField(max_length=5)  # French postal codes have 5 digits
    prof_ville = models.CharField(max_length=100)
    prof_tel_ecole = models.CharField(max_length=20)
    prof_tel_domicile = models.CharField(max_length=20, blank=True)  # Assuming this field can be optional
    prof_date_embauche = models.DateField()  # Dates should use the DateField type
    prof_date_depart = models.DateField(blank=True)

class Competences(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    libelle = models.CharField(max_length=100)
    description = models.TextField()

class TypeDeStages(models.Model):
    code_type = models.IntegerField(primary_key=True)  # Assuming that code_type is unique and can be used as a primary key.
    nb_semaines = models.PositiveIntegerField()


class Acquerir(models.Model):
    code = models.ManyToManyField(Competences)
    code_type = models.ManyToManyField(TypeDeStages)
    niv_exigence = models.IntegerField()

class Tuteurs(models.Model):
    tuteur_numero = models.CharField(max_length=10, primary_key=True)
    tuteur_entreprise = models.CharField(max_length=20)
    tuteur_qualite = models.CharField(max_length=10)
    tuteur_nom = models.CharField(max_length=100)
    tuteur_prenom = models.CharField(max_length=100)
    tuteur_telephone = models.CharField(max_length=20)



class Annees(models.Model):
    annee = models.IntegerField(primary_key=True)


class Entreprises(models.Model):
    n_siret = models.CharField(max_length=14, unique=True)  # SIRET numbers are 14 digits long
    forme_juridique = models.CharField(max_length=10)
    raison_sociale = models.CharField(max_length=200)
    entreprise_adresse = models.CharField(max_length=255)
    entreprise_suite = models.CharField(max_length=100, blank=True)  # optional
    entreprise_code_postal = models.CharField(max_length=5)  # French postal codes are 5 digits
    entreprise_ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    contact = models.CharField(max_length=100)
    tel_contact = models.CharField(max_length=20)


class inscriptions(models.Model):
    qualite = models.CharField(max_length=4)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    suite = models.CharField(blank=True, max_length=100)
    code_postal = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    sexe = models.DateField()
    Telephone = models.CharField(max_length=100)
    admis = models.BooleanField(default=False)

class effectuer(models.Model):
    code_type = models.ManyToManyField(TypeDeStages)
    annee = models.ManyToManyField(Annees)
    debut = models.DateField()
    fin = models.DateField()

class Associer(models.Model):
    n_tuteur = models.ManyToManyField(Tuteurs)
    n_siret = models.ManyToManyField(Entreprises)
class Promos(models.Model):
    annee = models.CharField(max_length=4, primary_key=True)  # Assuming annee is a year format YYYY
    nb_inscrit = models.IntegerField()
    nb_recus = models.IntegerField()
    prof_num = models.ForeignKey(Professeurs, on_delete=models.CASCADE,)

class Etudiants(models.Model):
    etudiant_promo = models.CharField(max_length=10, primary_key=True)
    etudiant_qualite = models.CharField(max_length=10)  # e.g., Mr, Mme, etc.
    etudiant_nom = models.CharField(max_length=100)
    etudiant_prenom = models.CharField(max_length=100)
    etudiant_adresse = models.CharField(max_length=255)
    etudiant_code_postal = models.CharField(max_length=5)  # French postal codes have 5 digits
    etudiant_ville = models.CharField(max_length=100)
    etudiant_sexe = models.CharField(max_length=1)  # M or F
    etudiant_naissance = models.DateField()  # Assuming a DateField for a date of birth
    etudiant_num_tel = models.CharField(max_length=20)
    etudiant_mention = models.CharField(max_length=50, blank=True,)  # Assuming this can be optional
    etudiant_annee = models.ForeignKey(Promos, on_delete=models.CASCADE)

class Stages(models.Model):
    in_stage = models.CharField(max_length=10, primary_key=True)
    compte_rendu = models.TextField(blank=True)  # Assuming this can be an optional field
    tuteur = models.ForeignKey(Tuteurs, on_delete=models.CASCADE)
    code_type = models.ForeignKey(TypeDeStages, on_delete=models.CASCADE)
    prof_num = models.ForeignKey(Professeurs, on_delete=models.CASCADE)
    siret = models.ForeignKey(Entreprises, on_delete=models.CASCADE)
    etudiant_promo = models.ForeignKey(Etudiants, on_delete=models.CASCADE)
    annee = models.ForeignKey(Promos, on_delete=models.CASCADE)