from django.contrib import admin

# Importar as classes
from .models import Campo, Atividade

# Register your models here.
admin.site.register(Campo)
admin.site.register(Atividade)