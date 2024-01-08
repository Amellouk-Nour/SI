from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_inscription(request):
    # return render(request,"")
    return HttpResponse("<h1>Inscription</h1>")

def index_connexion(request):
    # return render(request, "")
    return HttpResponse("<h1>connexion</h1>")
def index_change_mdp(request):
    # return render(request, "")
    return HttpResponse("<h1>change_mdp</h1>")

def index_connected(request):
    # return render(request, "")
    return HttpResponse("<h1>connected</h1>")


