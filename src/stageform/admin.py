from django.contrib import admin
from .models import *
# Register your models here.
class entrepriseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Entreprises, entrepriseAdmin)

class tuteurAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tuteurs, tuteurAdmin)