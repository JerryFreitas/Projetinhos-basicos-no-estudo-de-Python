num1 = float(input('Digite o primeiro número positivo: '))
num2 = float(input('Digite o segundo número positivo: '))

if num1 <= 0 or num2 <= 0:
    print('Os números informados devem ser positivos.')
else:
    print('Escolha uma opção:')
    print('1. Média ponderada, com pesos 2 e 3, respectivamente')
    print('2. Quadrado da soma dos 2 números')
    print('3. Cubo do menor número')
       
    opcao = int(input())
    
    if opcao == 1:
        media_ponderada = (2*num1 + 3*num2) / 5
        print('A média ponderada dos números é', media_ponderada,)
    elif opcao == 2:
        soma = num1 + num2
        quadrado_da_soma = soma**2
        print('O quadrado da soma dos números é', quadrado_da_soma,)
    elif opcao == 3:
        menor = min(num1, num2)
        cubo_do_menor = menor**3
        print('O cubo do menor número é', cubo_do_menor,)
    else:
        print('Opção inválida.')
