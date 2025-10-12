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

    def create(self, validated_data:dict) -> User:
        print("---- DADOS VALIDADADOS QUE CHEGARAM NO CREATE ----")
        print(validated_data)
        print("---------------------------------------------")
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