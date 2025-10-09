from django.shortcuts import render

from .service import LivroService
from .utils import get_status_error

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class LivroReadAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        service = LivroService(user=request.user)

        if pk:
            livro, error = service.get_all_livro_pk(pk)
            if error:
                status_error = get_status_error(error)
                return Response(error, status=status_error)
            return Response(livro, status=status.HTTP_200_OK)
        else: 
            livro, error = service.get_all_livro()
            if error:
                status_error = get_status_error(error)
                return Response(error, status=status_error)
            return Response(livro, status=status.HTTP_200_OK)
                
    
class LivroCreateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        service = LivroService(user=request.user)
        livro, error= service.create_livro(request.data)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(livro, status=status.HTTP_201_CREATED)

class LivroUpdateAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
 
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
    
class LivroDestroyAPIView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        service = LivroService(user=request.user)
        livro, error = service.delete_livro(pk)
        if error:
            status_error = get_status_error(error)
            return Response(error, status=status_error)
        return Response(status=status.HTTP_204_NO_CONTENT)
