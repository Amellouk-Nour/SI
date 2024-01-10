from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "SI_BD/index.html")
    # return HttpResponse("<p>hellon zakaria</p>")