from django.shortcuts import render, redirect, get_object_or_404
from .models import Ocorrencia
from .forms import OcorrenciaForm

def reportar(request):
    if request.method == 'POST':
        form = OcorrenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso') 
        
    else: # se for GET
        form = OcorrenciaForm()

    context = {
        'form': form
    }
    return render(request, 'ocorrencias/reportar.html', context)


def sucesso(request):
    return render(request, 'ocorrencias/sucesso.html')

def painel(request):
    ocorrencias = Ocorrencia.objects.all()
    context = {
        'ocorrencias': ocorrencias
    }
    return render(request, 'ocorrencias/painel.html', context)