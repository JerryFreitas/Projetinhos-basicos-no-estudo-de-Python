altura = float(input('Digite sua altura (em metros): '))
peso = float(input('Digite seu peso (em quilogramas): '))

imc = peso / altura**2


if imc < 18.5:
    situacao = 'abaixo do peso'
elif 18.5 <= imc < 25:
    situacao = 'com peso normal'
elif 25 <= imc < 30:
    situacao = 'com sobrepeso'
elif 30 <= imc < 35:
    situacao = 'com obesidade grau 1'
elif 35 <= imc < 40:
    situacao = 'com obesidade grau 2'
else:
    situacao = 'com obesidade grau 3'


print('Seu IMC é',imc, "Você está", situacao)
