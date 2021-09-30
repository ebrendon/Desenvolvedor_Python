dados_cliente = {                               # Declarando um dicionário
    'Nome': 'Franklyn',
    'Endereco': 'Rua de baixo',
    'Telefone': '999885437'
}  
print(dados_cliente)                            # Imprimindo todo o conteúdo do dicionário
dados_cliente.pop('Telefone', None)             # Removendo 'Telefone' do dicionário,

# o parâmetro None é usado para evitar erro caso a chave não exista
print(dados_cliente)  # Imprimindo dicionário alterado
