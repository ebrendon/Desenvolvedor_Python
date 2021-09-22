def calculo_imc(altura, peso):
    return(peso / pow(altura, 2))


altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
imc = calculo_imc(altura, peso)
print('O IMC é: ', imc)
if (imc <= 24.9 and imc >= 18.5):
    print('Peso normal')
elif (imc > 24.9):
    print('Sobrepeso')
else:
    print('abaixo do peso')
