from django import forms
from .models import Ocorrencia

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['categoria', 'descricao', 'localizacao', 'imagem']

        # Define tamanho do campo "Descriçao"
        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 4,
            }),
        }

# usado em: editar (painel)
class OcorrenciaEditForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['categoria', 'descricao', 'localizacao', 'imagem', 'status']

        widgets = {
            'descricao': forms.Textarea(attrs={
                'rows': 4,
            }),
        }
