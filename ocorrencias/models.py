from django.db import models

class Ocorrencia(models.Model):

    class CategoriaOcorrencias(models.TextChoices):
        CALCADA_BURACO = 'calcada_buraco', 'Calçada danificada / buraco'
        FIACAO_EXPOSTA = 'fiacao_exposta', 'Fiação exposta'
        LIXO_IRREGULAR = 'lixo_irregular', 'Lixo irregular'
        BUEIRO_ALAGAMENTO = 'bueiro_alagamento', 'Bueiro entupido / alagamento'
        FALTA_ILUMINACAO = 'falta_iluminacao', 'Falta iluminação'
        OUTROS = 'outros', 'Outros'


    class StatusOcorrencias(models.TextChoices):
        REPORTADO = 'reportado', 'Reportado'
        EM_ANALISE = 'em_analise', 'Em análise'
        RESOLVIDO = 'resolvido', 'Resolvido'

    categoria = models.CharField(max_length=50, choices=CategoriaOcorrencias.choices)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=155, help_text='Ex: Rua, Número, Bairro')
    # imagens serão salvas em media/ocorrencias/
    imagem = models.ImageField(upload_to='ocorrencias/%Y/%m/', blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=StatusOcorrencias.choices ,default=StatusOcorrencias.REPORTADO)


    def __str__(self):
        """Retorna o texto legível"""
        return f'{self.get_categoria_display()} - {self.localizacao}'