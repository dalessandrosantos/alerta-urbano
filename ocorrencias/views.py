from django.contrib.auth.decorators import login_required # Limita acesso a usuários logados
from django.contrib.auth.views import LoginView  # View pronta para login
from django.contrib import messages # Permite enviar avisos temporários para o usuário na tela

from django.shortcuts import render, redirect, get_object_or_404
from .models import Ocorrencia
from .forms import OcorrenciaForm, OcorrenciaEditForm

def reportar(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Reporte enviado com sucesso!" ) 
            return redirect('reportar')   
    else: # se for GET
        form = OcorrenciaForm()

    context = {
        'form': form,
    }
    return render(request, 'ocorrencias/reportar.html', context)


@login_required
def painel(request):
    ocorrencias = Ocorrencia.objects.all()
    context = {
        'ocorrencias': ocorrencias
    }
    return render(request, 'ocorrencias/painel.html', context)


@login_required
def editar(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)

    if request.method == 'POST':
        form = OcorrenciaEditForm(request.POST, request.FILES, instance=ocorrencia)

        if form.is_valid():
            form.save()
            return redirect('painel')

    else:
        form = OcorrenciaEditForm(instance=ocorrencia)

    context = {
        'ocorrencia': ocorrencia,
        'form': form,
    }
    return render(request, 'ocorrencias/editar.html', context)


@login_required
def deletar(request, pk):
    ocorrencia = get_object_or_404(Ocorrencia, pk=pk)

    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('painel')

    context = {
        'ocorrencia': ocorrencia
    }
    return render(request, 'ocorrencias/delete.html', context)


class LoginUsarioView(LoginView):
    template_name = 'registration/login.html'