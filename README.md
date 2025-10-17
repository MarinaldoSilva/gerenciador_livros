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

* **User**
  
  Endpoint de registro, em nosso user, temos 3 validações no ``extra_kwargs```onde tem regras no email, senha e username

  ```python
  extra_kwargs = {
            'password':{
                'write_only': True,
                'min_length': 8
            },
            'email':{
                'required':True,
                'allow_blank': False
            },
            'username': {
                'required': True,
                'allow_blank': False,
            }
        }
  ```
  
  ```bash
  http://127.0.0.1:8000/api/v1/user/registrar/
  ```

  ```json
  {
    "username": "Joyce_Hilpert72",
    "email": "Joyceh2000@gmail.com",
    "first_name": "Joice",
    "last_name": "Hilpert",
    "password": "hilperte201" 
  }
  ```


* **Livros**

* **GET**

endpoint:

```json
http://127.0.0.1:8000/api/v1/livros/1/
```

Se na nossa requisição for passado um PK/ID será retornado um item especifico, caso não seja, uma lista de elemtnos sera retornada.


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
Para cirar vários livros eu utilizei um random generate de dados ficticios para facilitar o processo de criação

```json
{
	"titulo":"{% faker 'randomJobTitle' %}",
	"autor": "{% faker 'randomFullName' %}",
	"genero": "{% faker 'randomJobDescriptor' %}"
}
```

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


O projeto em si preza pela segurança dos dados, o banco de dados tem que ser configurado localmente na sua máquina, são informações que são sensiveis e mesmo a aplicação sendo para fins de estudo, vou seguir as práticas de segurança adotadas pelo mercado de trabalho e analistas.

Criando ambiente virtual.

```bash
  python -m venv venv
  .\venv\Scipts\activate
```

instale o arquivido de libs:

```py
pip install -r requirements.txt
```
Faça as migrações para o banco

```py
    python manage.py migrate
```

Teste o serviço rodando o servidor próprio do Django.

```
   python manage.py runserver
```

Clone o projeto, gere uma nova chave `secret_key`, conecte seu banco e teste a aplicação.
