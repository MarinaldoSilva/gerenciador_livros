from .models import User
from typing import Any
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id', )
        """
        extra_kwargs
            Dicionário que recebe configurações extras para validação de campos
            write_only: True -> A senha recebida por escrito na requisição não sera retornada para visualização.
            min_length: n...n -> A senha tera pelo menos 8 digitos
            'required':True -> é obrigatório a passagem do campo
            'allow_blank': False -> Não pode ser um campo de string vazia
        """
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

        """
        quando uma metodo começa com 'validate_' e o nome de um campo especifico, o DRF invoca o validated para validar o campo especifico
        """
    def validate_email(self, value) -> Any:
        """
        se a operação for de criação ou atualização de um obj já existente o instance(o mesmo que passamos no metodo PATCH/PUT) é acionado, o self.instance vai conter a instancia do User que o invoca.
        caso seja para criar um do zero, o `self.instance` sera 'None'
        """
        if self.instance:
                """
                Entendendo o -> exclude(pk=self.instance.pk) quando vamos atualizar o email de um user, o próprio emaail dele é passado (email antigo), e com isso o sistema cairia no erro: 'Esse email já esta cadastrado.' mesmo sendo o email de quem enviou a requisição.
                quando excluimos com pk=self... estamos garantindo que se o email 'value' for igaul ao atual ele não ira causar erro, pois o email passado já é do próprio usuário, caso seja de outro user, o erro será disparado.
                filter(email=value): após excluir o usuário de quem requisitou, filtramos o resto dos email para verificar se já existe algum email assim cadastrado esse email, o email é um campo único, então se o usuário atualizar seu eamil com um email já cadastrado na base ira ocorrer um error.
                """
                if User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
                     raise serializers.ValidationError("Esse email já esta cadastrado.")
                else:
                    """
                    caso seja uma criação de usuário, o self.instance é None, e é verificado se o email já existe na base, o exclude não é necessário, pois não estamos com o usuário atual, estamos com um novo usuário e assim verificamos se o email já tem cadastro na base, o exists() retorna true ou false
                    """
                    if User.objects.filter(email=value).exists():
                        raise serializers.ValidationError("Esse email já esta cadastrado.") 
                return value #valor que foi envaido na requisição, pois as outras duas validações foram False
                    
    def validate_username(self, value) -> Any:
        if self.instance:
            if User.objects.exclude(pk=self.instance.pk).filter(username=value).exists():
                 raise serializers.ValidationError("Username em uso.")
            else:
                if User.objects.filter(username=value).exists():
                    raise serializers.ValidationError("Username em uso.")
            return value
    
    def create(self, validated_data:dict) -> User:
       
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''), 
            last_name=validated_data.get('last_name', '')
        )
        return user
    
    """instance é o obj que existe no bd e foi buscado para atualizar o usuário"""
    def update(self, instance, validated_data:dict):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        instance.username = validated_data.get("username",instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name) 
        instance.save()
        return instance