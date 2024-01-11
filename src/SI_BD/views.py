from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "SI_BD/index.html")
def red(request):
    return redirect("home")