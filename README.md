# API Biblioteca

Sistema de Cadastro com vinculo de usuário para listagem de livros, onde o usuário precisa fazer um cadastro (sem informações pessoais) para ter acesso ao seu acervo pessoal, todo processo é feito para evitar os erros mais
comuns de cadastro de usuário, mostrando mesnagens amigaveis em caso de algumas violações de validação e privacidade que o usuário tente fazer(atualizar/remover algo que outro usuário criou), as regras de segurança e validações foram feitas usando
o próprio django e DRF sem necessidade de Libs externas, mostrando assim o poder o Python e DRF.


## Funções:
* Buscar geral do usuário e ID
* criar
* Atualizar livro
* deletar livro

Foi usada uma classe de serviço chamada ``service``, a view não tem o contato diretamente com o serializer, não importa como os dados saõ processados ou como chegou lá, só importa os daods.

# EndPoints

* **Livros**
  
* **GET**

```py
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
```

* **POST**

```py
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
```


* **PUT**
  
```py
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
```

* **DELETE**

```py
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
```




Clone o projeto, gere uma nova chave `secret_key`, conecte seu banco e teste a aplicação.
