dados_cliente = {
    'Nome': 'Franklyn',
    'Endereco': 'Rua de baixo',
    'Telefone': '999885437'
}  # Declarando um dicionário
print(dados_cliente)  # Imprimindo todo o conteúdo do dicionário
dados_cliente.pop('Telefone', None)  # Removendo 'Telefone' do dicionário,
# o None é usado para evitar erro caso a chave não exista
print(dados_cliente)  # Imprimindo dicionário alterado
