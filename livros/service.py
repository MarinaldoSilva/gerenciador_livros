from .models import Livro
from .serializer import LivroSerializer
from .services.base_service import BaseLivroService
from typing import Any
from .services.types import (
    generic_service_response, delete_service_response,
    serializers_data, service_failured_response,
    errors_dict, service_success_response
    )

msg_error_status = "ID não localizado ou usuário sem permissão de acesso."
errors = "Errors"

class LivroService(BaseLivroService):

    def get_all_livro(self)-> generic_service_response:
        livros = Livro.objects.filter(dono=self.user)
        serializer = LivroSerializer(livros, many=True)
        return serializer.data, None
    
    def create_livro(self, data:dict[str, Any])-> generic_service_response:
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
    def get_all_livro_pk(self, pk:int) -> generic_service_response:
        try:
            livros = Livro.objects.get(pk=pk, dono=self.user)
            serializer = LivroSerializer(livros)
            return serializer.data, None
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        
    def update_livro(self, pk:int, data:dict[str, Any], partial=False) -> generic_service_response:
        try:
            livro = Livro.objects.get(pk=pk, dono=self.user)
        except Livro.DoesNotExist:
            return None, {errors:msg_error_status}
        serializer = LivroSerializer(instance=livro, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, None
        return None, serializer.errors
    
    def delete_livro(self, pk:int)-> delete_service_response:
        try:
            livro=Livro.objects.get(pk=pk, dono=self.user)
            livro.delete()
            return True, None
        except Livro.DoesNotExist:
            return False, {errors:msg_error_status}