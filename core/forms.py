from django import forms
from django.core.mail.message import EmailMessage

from core.models import Produto

""" 
    ContatoForm: 
        Criação de formulários HTML com Django, para envio de e-mails 
        após cadastro de produtos, sem vinculo ao Banco de Dados.
        Resumo: Disparo automático de e-mails após cadastro de produtos.

    ProdutoModelForm: 
        Criação de formulários HTML com Django, para cadastro de produtos
        no Banco de Dados, utilizando o modelo Produto.
"""

#11 - Formulário SEM integração ao Banco de Dados (forms.Form = definição de modelo manual)
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100) # label='Nome' define o rótulo do campo, max_length=100 limita o tamanho do texto
    email = forms.EmailField(label='E-mail', max_length=100) # EmailField valida se o texto é um e-mail válido
    assunto = forms.CharField(label='Assunto', max_length=120) # max_length=120 limita o tamanho do texto
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea()) # widget=forms.Textarea() permite que o campo seja um textarea

    def send_mail(self):
        nome = self.cleaned_data['nome'] # cleaned_data contém os dados validados do formulário
        email = self.cleaned_data['email'] # cleaned_data contém os dados validados do formulário
        assunto = self.cleaned_data['assunto'] # cleaned_data contém os dados validados do formulário
        mensagem = self.cleaned_data['mensagem'] # cleaned_data contém os dados validados do formulário

        '''self.cleaned_data[...] é um dicionário que o Django cria após validar os dados enviados no formulário'''

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        print(conteudo)

        #12 Enviando o e-mail
        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()


#11 - Formulário COM integração ao Banco de Dados  (forms.ModelForm = vinculado ao modelo Produto)
class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
