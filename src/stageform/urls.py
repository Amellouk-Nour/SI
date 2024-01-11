from django.urls import path
from .views import *

app_name = 'stageform'

urlpatterns = [
    path('createstage/', createstage, name='createstage'),
    path('statusstage/', statusstage, name='statusstage'),
    path('postuler/',stage_form_postuler,name='stage_form_postuler'),
    path('generate-pdf/', generate_pdf_view, name='generate_pdf')
]