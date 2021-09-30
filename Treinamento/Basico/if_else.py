'''

No python, o desvio condicional if funciona da seguinte forma:

"if condição:
	desvio    "

Para casos em que várias condições devem ser verificadas, utiliza-se o elif. Dessa forma:

"
if condição1:
	desvio1
elif condição2:
	desvio2
	.
	.
	.
elif condiçãoN:
	desvioN
"

Para casos de desvios incondicionais, pode-se utilizar o else. Da seguinte forma:

if condição1:
	desvio1
else:
	desvio
'''

# Abaixo segue um exemplo de um programa que calcula a média de um aluno
# Exemplificando a aplicação dos 3 tipos de desvio condicional

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1+nota2)/2
print('media: ', media)

if media >= 7.0:
	print('O aluno está aprovado!')
elif media >= 4.0 and media < 7.0:
	print('O aluno está de recuperação!')
else:
	print('O aluno está reprovado!')
