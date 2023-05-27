from django.contrib import admin
from .models import Categoria,Cliente,Filme,Locacao
# Register your models here.
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'data']
admin.site.register(Locacao)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Filme)
