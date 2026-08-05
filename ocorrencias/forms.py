from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['categoria', 'descricao', 'localizacao', 'imagem']

# usado em: editar (painel)
class OcorrenciaEditForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['categoria', 'descricao', 'localizacao', 'imagem', 'status']
        