from .models import Livro
from .serializer import LivroSerializer

msg_error_status = "ID não localizado ou usuário sem permissão de acesso."
errors = "Errors"

class LivroService:

    @staticmethod
    def get_livro_user(user):
        livros = Livro.objects.filter(dono=user)
        serializer = LivroSerializer(livros, many=True)
        return serializer.data, None
    
    @staticmethod
    def cadastrar_livro(data, user):
        try:
            serializer = LivroSerializer(data=data)
            if serializer.is_valid():
                serializer.save(dono=user)
                return serializer.data, None
            return None, serializer.errors
        except Livro.DoesNotExist:
            return None, {errors : msg_error_status}
        
        """
        LivroDetail
        """
    @staticmethod
    def get_all_livro_user(pk, user):
        try:
            livros = Livro.objects.get(pk=pk, dono=user)
            serializer = LivroSerializer(livros)
            return serializer.data, None
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        
    @staticmethod
    def update_livro(pk, data, user, partial=False):
        try:
            livro = Livro.objects.get(pk=pk, dono=user)
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        serializer = LivroSerializer(instance=livro, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    @staticmethod
    def deletar_livro(pk, user):
        try:
            livro=Livro.objects.get(pk=pk, dono=user)
            livro.delete()
            return True, None
        except Livro.DoesNotExist:
            return False, {errors:msg_error_status}