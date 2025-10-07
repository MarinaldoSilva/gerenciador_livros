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
        service = LivroService(user=request.user)
        livro, error = service.get_all_book_user()
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def post(self, request):
        service = LivroService(user=request.user)
        livro, error= service.create_book(request.data)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_201_CREATED)

class LivroDetail(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        service = LivroService(user=request.user)
        livro, error = service.get_all_book_user_pk(pk)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        service = LivroService(user=request.user)
        livro, error = service.update_livro(pk, request.data)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def patch(self, request, pk):
        service = LivroService(user=request.user)
        livro, error = service.update_livro(pk, request.data, partial=True)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        service = LivroService(user=request.user)
        livro, error = service.delete_book(pk)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(status=status.HTTP_204_NO_CONTENT)
