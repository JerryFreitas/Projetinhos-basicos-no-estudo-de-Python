a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c

if delta < 0:
    print('Não existem raízes reais.')
elif delta == 0:
    x = -b / (2*a)
    print('A única raiz real é.', x)
else:
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print('As raízes reais são',x1,'e',x2)
