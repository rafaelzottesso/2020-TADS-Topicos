from django.urls import path

# Importa as views que a gente criou
from .views import CampoCreate, StatusCreate, ClasseCreate, CampusCreate, AtividadeCreate
from .views import CampoUpdate, AtividadeUpdate
from .views import CampoDelete, AtividadeDelete
from .views import CampoList, AtividadeList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/campus/', CampusCreate.as_view(), name="cadastrar-campus"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),

    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name='editar-campo' ),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name='editar-atividade'),

    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name='excluir-campo' ),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name='excluir-atividade'),

    path('listar/campos/', CampoList.as_view(), name='listar-campos'),
    path('listar/atividades/', AtividadeList.as_view(), name='listar-atividades'),

]
