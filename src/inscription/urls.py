from django.urls import path
from .views import *

urlpatterns = [
    # path('sign-in/',index_inscription, name='inscription'),
    path('connexion/',index_connexion, name='connection'),
    path('utilisateur-x/change_mdp/',index_change_mdp, name=f'change_mdp'),# probleme mauvais javascript
    path('utilisateur-x/', index_connected, name=f'connected'),
    path('utilisateur-x/postuler/',index_postuler,name='postuler')

]