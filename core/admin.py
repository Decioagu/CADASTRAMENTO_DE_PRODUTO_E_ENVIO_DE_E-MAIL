from django.contrib import admin

from core.models import Produto

#11 Registrando o modelo Produto no Django Admin
@admin.register(Produto) # Decorador para registrar o modelo Produto
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')
