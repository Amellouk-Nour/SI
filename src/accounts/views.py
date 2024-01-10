from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import unauthenticated_user, allowed_users
from inscription.models import inscriptions

@unauthenticated_user
def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # email = request.POST['email']
        user = authenticate(username=username, password=password)



        if user is not None:
            login(request, user)
            firstname = user.first_name
            return redirect('home')
        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')
    form = AuthenticationForm()
    return render(request, 'accounts/auth page.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirmpwd = request.POST['comfirmpwd']

        if password == confirmpwd:
            my_user = User.objects.create_user(username, email, password)
            my_user.first_name = firstname
            my_user.last_name = lastname
            my_user.is_active = True
            my_user.save()

        qualite = request.POST.get('qualite')
        nom = request.POST.get('lastname')
        prenom = request.POST.get('firstname')
        address = request.POST.get('address')
        suite = request.POST.get('suite')
        code_postal = request.POST.get('code_postal')
        ville = request.POST.get('ville')
        sexe = request.POST.get('sexe')
        date_naissance = request.POST.get('date_naissance')
        telephone = request.POST.get('telephone')

        new_inscription = inscriptions(qualite=qualite, nom=nom, prenom=prenom, adress=address, suite=suite,
                                       code_postal=code_postal, ville=ville, sexe=sexe, date_naissance=date_naissance,
                                       telephone=telephone, admis=False)
        new_inscription.save()
        return redirect("home")

    return render(request, 'accounts/register page.html')
