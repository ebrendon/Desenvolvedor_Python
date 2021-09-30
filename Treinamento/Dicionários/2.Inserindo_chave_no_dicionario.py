"""
Ao inserir um valor em um índice que não existe no dicionário
Esse índice será criado e inserido no final do dicionário.
"""


dados_cliente = {											# Declarando um dicionário
    'Nome': 'Franklyn',
    'Endereco': 'Rua de baixo',
    'Telefone': '999885437'
}  
print(dados_cliente)  										# Imprimindo todo o conteúdo do dicionário
dados_cliente['Idade'] = 40                                 # Inserindo uma nova chave e seu valor
print(dados_cliente)                                        # Imprimindo dicionário alterado
