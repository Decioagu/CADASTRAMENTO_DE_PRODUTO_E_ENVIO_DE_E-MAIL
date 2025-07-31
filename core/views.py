from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from core.forms import ContatoForm, ProdutoModelForm
from core.models import Produto

#11 - Conexão entre HTML e Banco de Dados
def index(request): 
    context = {
        # Obtendo todos os produtos do banco de dados 
        'produtos': Produto.objects.all() # "models.py"
    }
    return render(request, 'index.html', context)

'''
    ContatoForm: 
        Criação de formulários HTML com Django, para envio de e-mails 
        após cadastro de produtos, sem vinculo ao Banco de Dados.
        Resumo: Disparo automático de e-mails após cadastro de produtos.
'''
#11 - Conexão entre HTML e Banco de Dados
def contato(request):
    # Cria o formulário com os dados do POST ou vazio se não houver dados 
    form = ContatoForm(request.POST or None) # "forms.py"

    if str(request.method) == 'POST':
        if form.is_valid(): # Verifica se o formulário é válido (metodo)

            # Envia o e-mail usando o método send_mail do formulário
            form.send_mail() # "forms.py"

            messages.success(request, 'E-mail enviado com sucesso!') # Exibe uma mensagem de sucesso

            # Reseta o formulário para vazio após o envio bem-sucedido
            form = ContatoForm() # "forms.py"
        else:
            messages.error(request, 'Erro ao enviar e-mail') # Exibe uma mensagem de erro
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

'''
    ProdutoModelForm: 
        Criação de formulários HTML com Django, para cadastro de produtos
        no Banco de Dados, utilizando o modelo Produto.
'''
#11 - Conexão entre HTML e Banco de Dados
def produto(request):
    if str(request.user) != 'AnonymousUser': # Verifica se o usuário está autenticado
        if str(request.method) == 'POST': # Verifica se o método da requisição é POST
            
            # Cria o formulário com os dados do POST e arquivos (imagens)
            form = ProdutoModelForm(request.POST, request.FILES) # "forms.py"
            if form.is_valid(): # Verifica se o formulário é válido (metodo)
                
                form.save() # Salva o formulário no banco de dados (metodo)

                messages.success(request, 'Produto salvo com sucesso.') # Exibe uma mensagem de sucesso se o formulário for válido

                # Reseta o formulário para vazio após o salvamento bem-sucedido
                form = ProdutoModelForm() # "forms.py"
            else:
                messages.error(request, 'Erro ao salvar produto.') # Exibe uma mensagem de erro se o formulário não for válido
        else:
            # Cria um formulário vazio se não for uma requisição POST
            form = ProdutoModelForm() # "forms.py"
        context = {
            'form': form
        }
        # Renderiza a página de produto com o formulário
        return render(request, 'produto.html', context) 
    else:
        # Redireciona para a página inicial se o usuário não estiver autenticado
        return redirect('index') 
