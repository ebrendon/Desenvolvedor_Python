'''
A estrutura de repetição for segue a função range(), a qual cumpre a função de contagem.
Dessa forma, temos o seguinte esqueleto para o laço de repetição:

"
for contador in range (inicio, fim, passo):
	passos
"

Onde:

contador = é uma variável temporária (não necessita ser declarada previamente)
inicio = é o inicio do intervalo atribuido ao laço de repetição
fim = é o fim do intervalo atribuido ao laço de repetição
passo = é a contagem de quanto em quanto será percorrido esse intervalo
ex: passo = 2. Contagem de 2 em 2.


Obs = Caso queira contar do final para o começo, deve-se utilizar um passo negativo
ex: for c in range(6,0,-2):
		ação

Nesse exemplo, o laço irá iterar do 6 ao zero pulando de 2 em 2.
'''

#O programa exemplo apresenta uma contagem regressiva para o usuário

for c in range(10, 0, -1):
	print(c)
print("Booom!")
