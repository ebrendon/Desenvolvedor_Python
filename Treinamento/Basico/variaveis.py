'''
Existem 4 tipos primitivos no python:


# Int: é o tipo que representa os números inteiros. (...,-2, -1, 0, 1, 2, ...)
# Float: é o tipo que representa os números reais com casas decimais. (..., -1.02, -1.01, -1, 0, 1, 1.01, 1.02, …)
# Bool: é o tipo que representa os valores booleanos. (True, False)
# String: é o tipo que representa as cadeias de caracteres. (nomes, palavras, etc.)

A estrutura utilizada para a declaração de variáveis no Python é a seguinte:

nome_da_variavel = tipo_da_variavel(input('Texto a ser apresentado para o usuário'))

ex:

nome_da_variavel = int(input('Texto a ser apresentado para o usuário'))
nome_da_variavel = float(input('Texto a ser apresentado para o usuário'))
nome_da_variavel = str(input('Texto a ser apresentado para o usuário'))

Obs: é possível declarar variáveis sem definir o seu tipo, apesar de não ser
	 recomendado. Nesses casos, o interpretador considera a variável como se 
	 fosse do tipo str.



Para apresentar os valores armazenados na variável para o usuário
utiliza-se a seguinte estrutura:

print('Texto {1} texto {2} texto {3}'.format(nome_da_variavel1, nome_da_variavel2, nome_da_variavel3))

Onde o simbolo {} serve como uma chave que será substituida pelo valor da variável correspondente
'''

#O programa a seguir, armazena dados básicos do usuário e os apresenta na tela

nome = str(input('Digite seu nome: '))					
idade = int(input('Digite sua idade: '))			
altura = float(input('Digite sua altura: '))
cidade = input('Digite sua cidade atual: ')				# como dito acima, o interpretador irá considerar essa variável
														# como uma string


print('O usuário cujos dados: ')
print('Nome: {}, Idade: {}, altura: {}'.format(nome, idade, altura))
print('Original da cidade {}'.format(cidade))