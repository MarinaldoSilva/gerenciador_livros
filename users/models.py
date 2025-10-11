from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    email = models.EmailField(unique=True, blank=False, null=False)
    
    class Meta:
        verbose_name= "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.username}"



