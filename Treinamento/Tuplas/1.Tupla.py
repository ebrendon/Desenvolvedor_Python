'''
Tupla é um tipo especial de Lista cujos itens não podem ser alterados após a sua inserção.
Ou seja, não será possível adicionar, remover itens ou  alterar sua ordem dentro da tupla.
Dessa forma, o unico momento em que pode-se inserir itens em uma tupla é quanto ela está
vazia.

A declaração de uma tupla se dá das seguintes formas:

nome_da_tupla = (valor1, valor2, valor3)

ou

nome_da_tupla = tuple()  											#Cria uma tupla vazia

'''

lanche = ('pastel', 'coxinha', 'suco', 'pudim')  					# Declaração de uma tupla
print(type(lanche))  												# Imprime o tipo da variável
print(lanche)  														# Imprime todo o conteúdo da tupla
print(lanche[3])  													# Imprime o índice 3 que equivale ao elemento 'pudim'
print(lanche[:2])  													# Imprime os elementos anteriores ao índice 2
