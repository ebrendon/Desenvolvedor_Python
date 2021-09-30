dados_cliente = {                                   # Declarando um dicionário
    'Nome': 'Franklyn',
    'Endereco': 'Rua de baixo',
    'Telefone': '999885437'
}  
print(dados_cliente)                                # Imprimindo todo o conteúdo do dicionário
del dados_cliente['Telefone']                       # Deletando a chave 'Telefone' e seu conteúdo
print(dados_cliente)                                # Imprimindo dicionário alterado
