
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Motorista, Passageiro, Corrida
from .forms import CorridaForm

# Create your views here.


@login_required
def home(request):

    context = {
        "count_motoristas": Motorista.objects.count(),
        "count_passageiros": Passageiro.objects.count(),
        "count_corridas": Corrida.objects.count(),
    }

    return render(request, 'core/home.html', context)


class MotoristaList(LoginRequiredMixin, ListView):
    model = Motorista


class MotoristaCreate(LoginRequiredMixin, CreateView):
    model = Motorista
    success_url = reverse_lazy('core:motorista_list')
    fields = ['name', "birth_date", "cpf", "sexo", "model_car", 'active']


class MotoristaUpdate(LoginRequiredMixin, UpdateView):
    model = Motorista
    success_url = reverse_lazy('core:motorista_list')
    fields = ['name', "birth_date", "cpf", "sexo", "model_car", 'active']


class MotoristaDelete(LoginRequiredMixin, DeleteView):
    model = Motorista
    success_url = reverse_lazy('core:motorista_list')


class PassageiroList(LoginRequiredMixin, ListView):
    model = Passageiro


class PassageiroCreate(LoginRequiredMixin, CreateView):
    model = Passageiro
    success_url = reverse_lazy('core:passageiro_list')
    fields = ['name', "birth_date", "cpf", "sexo"]


class PassageiroUpdate(LoginRequiredMixin, UpdateView):
    model = Passageiro
    success_url = reverse_lazy('core:passageiro_list')
    fields = ['name', "birth_date", "cpf", "sexo"]


class PassageiroDelete(LoginRequiredMixin, DeleteView):
    model = Passageiro
    success_url = reverse_lazy('core:passageiro_list')


class CorridaList(LoginRequiredMixin, ListView):
    model = Corrida


class CorridaCreate(LoginRequiredMixin, CreateView):
    model = Corrida
    form_class = CorridaForm
    success_url = reverse_lazy('core:corrida_list')
