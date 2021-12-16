from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Magazine)
admin.site.register(CategoriaMagazine)
admin.site.register(TipoArtigo)
admin.site.register(Artigo)
admin.site.register(TipoErro)
admin.site.register(ReportarErro)