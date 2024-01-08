from django.urls import path
from .views import index_inscription, index_connexion, index_change_mdp, index_connected

urlpatterns = [
    path('sign-in/',index_inscription, name='inscription'),
    path('connexion/',index_connexion, name='connection'),
    path('utilisateur-x/change_mdp',index_change_mdp, name=f'change_mdp'),
    path('utilisateur-x/', index_connected, name=f'connected')

]