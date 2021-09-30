"""
Dicionário é um tipo especial de lista onde seus índices podem recerber nomes e não apenas números.

Eles podem ser declarados das seguintes formas:

nome_do_dicionario = {
						'indice1': 'valor'
						'indice2': 'valor'
						'indice3': 'valor'
					 }

ou

nome_do_dicionario = dict()									#Cria um dicionário vazio
"""

dados_cliente = {											# Declarando um dicionário
    'Nome': 'Franklyn',
    'Endereco': 'Rua de baixo',
    'Telefone': '999885437'
}  
print(type(dados_cliente))  								# Imprimindo o tipo da variável
print(dados_cliente) 										# Imprimindo todo o conteúdo do dicionário
print(dados_cliente['Endereco'])  							# Imprimindo o conteúdo da chave 'Endereço'

dados_cliente.keys()										# Retornando as chaves do dicionário
dados_cliente.values()										# Retornando os valores armazenados no dicionário
dados_cliente.items()										# Retornando uma lista de tuplas, onde cada tupla é composta pela
															# chave e pelo seu valor associado, respectivamente.
