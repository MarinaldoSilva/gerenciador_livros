from .models import Livro
from .serializer import LivroSerializer

msg_error_status = "ID não localizado ou usuário sem permissão de acesso."
errors = "Errors"

class LivroService:

    def __init__(self, user):
        self.user = user

    def get_all_book_user(self):
        livros = Livro.objects.filter(dono=self.user)
        serializer = LivroSerializer(livros, many=True)
        return serializer.data, None
    
    def create_book(self, data):
        try:
            serializer = LivroSerializer(data=data)
            if serializer.is_valid():
                serializer.save(dono=self.user)
                return serializer.data, None
            return None, serializer.errors
        except Livro.DoesNotExist:
            return None, {errors : msg_error_status}
        
        """
        LivroDetail
        """
    def get_all_book_user_pk(self, pk):
        try:
            livros = Livro.objects.get(pk=pk, dono=self.user)
            serializer = LivroSerializer(livros)
            return serializer.data, None
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        
    def update_livro(self, pk, data, partial=False):
        try:
            livro = Livro.objects.get(pk=pk, dono=self.user)
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        serializer = LivroSerializer(instance=livro, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    def delete_book(self, pk):
        try:
            livro=Livro.objects.get(pk=pk, dono=self.user)
            livro.delete()
            return True, None
        except Livro.DoesNotExist:
            return False, {errors:msg_error_status}