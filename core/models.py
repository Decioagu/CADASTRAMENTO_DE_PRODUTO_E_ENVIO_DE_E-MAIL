from django.db import models
from django.db.models import signals
from stdimage.models import StdImageField
from django.template.defaultfilters import slugify

""" 
    Criando o modelo Base e o modelo Produto com herança em Django.
    Resumo: Implementação de um modelo base para reutilização de campos comuns 
    e criação de um único modelo.

    - Criação de tabela: 
        - core_produto

    - Descrição:
        - Modelo Base: Contém campos comuns como "criação", "modificação" e "ativo".
        - Modelo Produto: Herda do modelo Base e adiciona campos específicos como "nome", 
        "preço", "estoque", "imagem" e "slug".
"""

#11 Criando o modelo base para os outros modelos
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

#11 Criando o modelo Produto que herda de Base
class Produto(Base): # Herança do modelo Base
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False) # slug é um identificador amigável para URLs

    def __str__(self):
        return self.nome

#11 Criando o método pre_save para gerar o slug automaticamente
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome) # Gera o slug a partir do nome do produto


signals.pre_save.connect(produto_pre_save, sender=Produto) # Conecta o sinal pre_save ao método produto_pre_save para gerar o slug automaticamente antes de salvar o produto

