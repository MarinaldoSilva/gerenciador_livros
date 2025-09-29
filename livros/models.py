from django.db import models
from django.conf import settings


class Livro(models.Model):

    dono = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='livro')

    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(blank=True, null=True)
    dt_publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor} em {self.dt_publicacao}"
    
    

