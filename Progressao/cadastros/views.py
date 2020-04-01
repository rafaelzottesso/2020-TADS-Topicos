from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campo, Atividade, Status, Classe, Campus

from django.urls import reverse_lazy

# Create your views here.


class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')


class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')


################# UPDATE #################

class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campos')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class ClasseUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')


class CampusUpdate(UpdateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')

################# DELETE #################


class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campos')


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


class StatusDelete(DeleteView):
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')


class ClasseDelete(DeleteView):
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classe')


class CampusDelete(DeleteView):
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campus')


################# LISTA #################


class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'


class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'


class StatusList(ListView):
    model = Status
    template_name = 'cadastros/listas/status.html'


class ClasseList(ListView):
    model = Classe
    template_name = 'cadastros/listas/classe.html'


class CampusList(ListView):
    model = Campus
    template_name = 'cadastros/listas/campus.html'
