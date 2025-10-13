# API Biblioteca

Sistema de Cadastro com vinculo de usuário para listagem de livros, onde o usuário precisa fazer um cadastro (sem informações pessoais) para ter acesso ao seu acervo pessoal, todo processo é feito para evitar os erros mais
comuns de cadastro de usuário, mostrando mesnagens amigaveis em caso de algumas violações de validação e privacidade que o usuário tente fazer(atualizar/remover algo que outro usuário criou), as regras de segurança e validações foram feitas usando
o próprio django e DRF sem necessidade de Libs externas, mostrando assim o poder o Python e DRF.


## Funções:
* Buscar geral do usuário e ID
* criar
* Atualizar livro
* deletar livro

Clone o projeto, gere uma nova chave `secret_key`, conecte seu banco e teste a aplicação.
