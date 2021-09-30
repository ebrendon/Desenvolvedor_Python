'''
Para retornar um valor obtido em uma função, utiliza-se a palavra reservada Return:

ex:

    def nome_da_funcao(parametros):
        funcionalidades da função
        return valor_obtido
'''


def calculo_imc(altura, peso):                          #função que realiza o cálculo do imc
    return(peso / pow(altura, 2))                       #retorna o valor obtido para o ponto em que a função foi chamada inicialmente


altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
imc = calculo_imc(altura, peso)                         #armazena na variável "imc" o valor obtido após a chamada da função calculo_imc()
print('O IMC é: ', imc)
if (imc <= 24.9 and imc >= 18.5):
    print('Peso normal')
elif (imc > 24.9):
    print('Sobrepeso')
else:
    print('abaixo do peso')
