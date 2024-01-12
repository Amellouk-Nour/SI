from django.urls import path
from .views import createstage, statusstage, stage_form_postuler, generate_pdf_view, upload
from django.conf import settings
from django.conf.urls.static import static
app_name = 'stageform'

urlpatterns = [
    path('createstage/', createstage, name='createstage'),
    path('statusstage/', statusstage, name='statusstage'),
    path('postuler/',stage_form_postuler,name='stage_form_postuler'),
    path('generate-pdf/', generate_pdf_view, name='generate_pdf'),
    path('upload/', upload, name='upload_file'),

]