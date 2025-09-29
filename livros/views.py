from django.shortcuts import render

from .service import LivroService
from .utils import get_status_error

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LivroListCreateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        livro, error = LivroService.get_livro_user(request.user)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def post(self, request):
        livro, error= LivroService.cadastrar_livro(request.data, request.user)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_201_CREATED)

class LivroDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        livro, error = LivroService.get_all_livro_user(pk, request.user)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        livro, error = LivroService.update_livro(pk, request.data, request.user)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        livro, error = LivroService.update_livro(pk, request.data, request.user, partial=True)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        livro, error = LivroService.deletar_livro(pk, request.user)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(status=status.HTTP_204_NO_CONTENT)

def homepage_view(request):
    return render(request, 'livros/index.html')