'''
Para a estrutura de repetição while, utiliza-se a seguinte estrutura:

"
while condição:
	execute
"

Para casos de loop infinito, utiliza-se o comando "break" como
condição de parada.

ex:

"
while True:
	if condição:
		break
"

'''

#O programa exemplo a seguir, calcula o fatorial do número digitado pelo usuário

num = int(input('Digite o número fatorial desejado: '))

c = num
fat = 1

while c > 0:

	fat *= c						
	c -= 1							#Não existe o operador de incremento (++) ou decremento (--) em Python

print('O fatorial desejado é igual a: {}'.format(fat))