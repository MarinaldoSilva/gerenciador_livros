from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from typing import Union, List, Dict, Tuple, Optional, Any
"""
esse padão de tipos é chamado de type Aliases, são 'atalhos', ao inves de ter uma
tipagem gigante, podemos separar essa responsábilidade da mesmoa forma que foi separada a questão dos 
retornos de status http
ReturnDict, ReturnList => Retornos de uma classe que tem retorno de um dict ou list
Union = pode ter alguns valores[a,b ou c,a e etc...],
Tuple, List ou Dict = retorna uma tupla, lista ou dicionário
Optional = funciona como um atalho de Union, se passar somente um parametro o 2º é None,
ex.: Optional[list] == Union[List, None]
"""

serializers_data = Union[ReturnDict, ReturnList, Dict[str, Any]]
"""
1º pode ser retornado uma lista de dicionarios, podemos ter vários itens serializados
o famoso many=True que usamos no listar
2º pode ser retornado uma lista de dados, onde teremos somente 1 item serializado
3º retorna algo mais generico, o par vai ter a chave string e o valor da chave pode ser qualquer outro
usamos para os dados do request.data assim podemos ser flexivies.
"""
errors_dict = Union[ReturnDict, Dict[str, any]]
"""
um retorno de erro pode retornar um valor padrão com 'chave:valor' ou um dict com uma string e com um valor qualquer no conteudo da chave string
"""

service_success_response = Tuple[serializers_data, None]
"""se o nosso service tiver sucesso, o retorno vai ser o nosso serializer.data e None indicando que nossa solicitação foi atendida"""
service_failured_response = Tuple[None, errors_dict]
"""o oposto do sucesso, se tiver erro, vem o None e após isso o dict erros"""

generic_service_response = Union[service_success_response, service_failured_response]

delete_service_response = Union[Tuple[bool,None], Tuple[bool, errors_dict]]

"""
os metodos do service tem duas repostas possivies serializer.dato, None ou None, serializer.errors
por isso os todos os possíveis valores de retorno tem pelo menos 2 valores
"""