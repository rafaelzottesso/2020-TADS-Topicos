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
    success_url = reverse_lazy('listar-campos')


class AtividadeCreate(CreateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class ComprovanteCreate(CreateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovantes')


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
    success_url = reverse_lazy('listar-campos')


class AtividadeUpdate(UpdateView):
    model = Atividade
    fields = ['numero', 'descricao', 'pontos', 'detalhes', 'campo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-atividades')


class ComprovanteUpdate(UpdateView):
    model = Comprovante
    fields = ['progressao', 'atividade',
              'quantidade', 'data', 'data_final', 'arquivo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comprovantes')


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
    success_url = reverse_lazy('listar-campos')


class AtividadeDelete(DeleteView):
    model = Atividade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-atividades')


class ComprovanteDelete(DeleteView):
    model = Comprovante
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comprovantes')


class ValidacaoDelete(DeleteView):
    model = Validacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-validacoes')


################# LISTA #################


class CampusList(ListView):
    model = Campus
    template_name = 'cadastros/campus.html'


class StatusList(ListView):
    model = Status
    template_name = 'cadastros/status.html'


class SituacaoList(ListView):
    model = Situacao
    template_name = 'cadastros/situacao.html'


class ClasseList(ListView):
    model = Classe
    template_name = 'cadastros/classe.html'


class ProgressaoList(ListView):
    model = Progressao
    template_name = 'cadastros/progressao.html'


class CampoList(ListView):
    model = Campo
    template_name = 'cadastros/campo.html'


class AtividadeList(ListView):
    model = Atividade
    template_name = 'cadastros/atividade.html'


class ComprovanteList(ListView):
    model = Comprovante
    template_name = 'cadastros/comprovante.html'


class ValidacaoList(ListView):
    model = Validacao
    template_name = 'cadastros/validacao.html'
