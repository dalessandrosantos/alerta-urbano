from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    model = Ocorrencia
    fields = ['categoria', 'descricao', 'localizacao', 'imagem']