from django.contrib import admin
from .models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo','autor','genero','dt_publicacao','dono']
    search_fields = ['titulo', 'autor', 'dono__username']
