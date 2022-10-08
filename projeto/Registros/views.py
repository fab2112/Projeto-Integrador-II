# Registros/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied, RequestAborted
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Registro, Comentario, Recebido
from django.shortcuts import render
from django.http import HttpResponse


def pesquisa_list_view(request):
    queryset = Registro.objects.all()
    pesquisa = request.GET['pesquisa']
    return render(request, 'pesquisa_listagem.html', {'pesquisa': pesquisa, "object_list": queryset})


class RegistroListViewAll(ListView):
    model = Registro
    template_name = 'registro_listagem_all.html'


class RegistroListView(LoginRequiredMixin, ListView):
    template_name = 'registro_listagem.html'
    login_url = 'login'

    def get_queryset(self):
        return Registro.objects.all()  # object_list

    def get_context_data(self, **kwargs):
        context = super(RegistroListView, self).get_context_data(**kwargs)
        context['recebido_list'] = Recebido.objects.all
        return context


class RegistroDetailView(LoginRequiredMixin, DetailView):
    model = Registro
    template_name = 'registro_detail.html'
    login_url = 'login'


class RegistroUpdateView(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ('doacao', 'contato', 'endereco', 'obs')
    template_name = 'registro_edicao.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.doador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RegistroCommentView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ('comentario',)
    template_name = 'registro_comentario.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.registro_id = self.kwargs['pk']
        return super().form_valid(form)


class RegistroDeleteView(LoginRequiredMixin, DeleteView):
    model = Registro
    template_name = 'registro_delecao.html'
    success_url = reverse_lazy('registro_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.doador != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class RegistroRecebidoView(LoginRequiredMixin, CreateView):
    model = Recebido
    fields = ('contato_2',)
    template_name = 'registro_recebido.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.receptor = self.request.user
        form.instance.recebido_id = self.kwargs['pk']

        registro = Registro.objects.get(id=form.instance.recebido_id)
        if registro.doador == self.request.user:
            raise PermissionDenied
        else:
            registro.status = False
            registro.save()
        return super().form_valid(form)


class RegistroCreateView(LoginRequiredMixin, CreateView):
    model = Registro
    template_name = 'registro_novo.html'
    fields = ('doacao', 'contato', 'endereco', 'obs', 'image')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.doador = self.request.user
        form.save()
        return super().form_valid(form)


class RegistroUpdateRecebidoView(LoginRequiredMixin, UpdateView):
    model = Registro
    fields = ('status',)
    template_name = 'registro_status_update.html'
    login_url = 'login'
    success_url = reverse_lazy('registro_list_all')

    def form_valid(self, form):
        form.instance.recebido_id = self.kwargs['pk']
        change_registro_status = Registro.objects.get(id=form.instance.recebido_id)
        change_registro_status.status = True
        change_registro_status.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'comentario_delecao.html'
    success_url = reverse_lazy('registro_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.autor != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
