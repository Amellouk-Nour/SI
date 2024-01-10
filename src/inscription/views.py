from django.http import HttpResponse
from django.shortcuts import render
from .models import inscriptions

# Create your views here.
def index_postuler(request):
    if request.method == 'POST':
        qualite = request.POST.get('qualite')
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        address = request.POST.get('address')
        suite = request.POST.get('suite')
        code_postal = request.POST.get('code_postal')
        ville = request.POST.get('ville')
        sexe = request.POST.get('sexe')
        date_naissance = request.POST.get('date_naissance')
        telephone = request.POST.get('telephone')

        new_inscription = inscriptions(qualite=qualite, nom=nom, prenom=prenom, adress=address, suite=suite, code_postal=code_postal, ville=ville, sexe=sexe, date_naissance=date_naissance, telephone=telephone, admis=False)
        new_inscription.save()
    return render(request,"inscription/register page.html")

def index_connexion(request):
    return render(request, "inscription/auth page.html")
def index_change_mdp(request):
    return render(request, "inscription/chang pass.html")


def index_connected(request):
    # return render(request, "")
    return HttpResponse("<h1>connected</h1>")




