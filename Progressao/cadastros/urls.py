from django.urls import path

# Importa as views que a gente criou
from .views import CampoCreate, StatusCreate, ClasseCreate, CampusCreate, AtividadeCreate

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/campus/', CampusCreate.as_view(), name="cadastrar-campus"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
]
