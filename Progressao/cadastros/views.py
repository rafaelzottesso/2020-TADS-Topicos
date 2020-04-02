from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Campus, Servidor, Status, Situacao, Classe, Progressao, Campo, Atividade, Comprovante, Validacao

from django.urls import reverse_lazy

# Create your views here.


class CampusCreate(CreateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')


class StatusCreate(CreateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class SituacaoCreate(CreateView):
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseCreate(CreateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')


class ProgressaoCreate(CreateView):
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')


class CampoCreate(CreateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'pontos', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')


class ComprovanteCreate(CreateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovante')


class ValidacaoCreate(CreateView):
    model = Validacao
    fields = ['quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')


################# UPDATE #################

class CampusUpdate(UpdateView):
    model = Campus
    fields = ['cidade', 'endereco', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campus')


class ServidorUpdate(UpdateView):
    model = Servidor
    fields = ['nome_completo', 'siape', 'cpf', 'campus']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class StatusUpdate(UpdateView):
    model = Status
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-status')


class SituacaoUpdate(UpdateView):
    model = Situacao
    fields = ['status', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseUpdate(UpdateView):
    model = Classe
    fields = ['nome', 'nivel', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-classe')


class ProgressaoUpdate(UpdateView):
    model = Progressao
    fields = ['classe', 'data_inicial', 'data_final', 'observacao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-progressao')


class CampoUpdate(UpdateView):
    model = Campo
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['campo', 'numero', 'descricao', 'pontos', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividade')


class ComprovanteUpdate(UpdateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovante')


class ValidacaoUpdate(UpdateView):
    model = Validacao
    fields = ['quantidade', 'justificativa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-validacoes')


################# DELETE #################


class CampusDelete(DeleteView):
    model = Campus
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campus')


class StatusDelete(DeleteView):
    model = Status
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-status')


class SituacaoDelete(DeleteView):
    model = Situacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-situacao')


class ClasseDelete(DeleteView):
    model = Classe
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-classe')


class ProgressaoDelete(DeleteView):
    model = Progressao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-progressao')


class CampoDelete(DeleteView):
    model = Campo
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-campo')


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividade')


class ComprovanteDelete(DeleteView):
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovante')


class ValidacaoDelete(DeleteView):
    model = Validacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-validacao')


################# LISTA #################


class CampusList(ListView):
    model = Campus
    template_name = 'cadastros/listas/campus.html'


class StatusList(ListView):
    model = Status
    template_name = 'cadastros/listas/status.html'


class SituacaoList(ListView):
    model = Situacao
    template_name = 'cadastros/listas/situacao.html'


class ClasseList(ListView):
    model = Classe
    template_name = 'cadastros/listas/classe.html'


class ProgressaoList(ListView):
    model = Progressao
    template_name = 'cadastros/listas/progressao.html'


class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/listas/campo.html'


class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/listas/atividade.html'


class ComprovanteList(ListView):
    model = Comprovante
    template_name = 'cadastros/listas/comprovante.html'


class ValidacaoList(ListView):
    model = Validacao
    template_name = 'cadastros/listas/validacao.html'
