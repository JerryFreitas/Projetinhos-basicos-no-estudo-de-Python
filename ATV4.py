
login1 = {'usuario': 'procopio', 'senha': '12345'}
login2 = {'usuario': 'paiva', 'senha': '54321'}


usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')


if (usuario == login1['usuario'] and senha == login1['senha']) or (usuario == login2['usuario'] and senha == login2['senha']):
    print('Seja bem-vindo!')
else:
    print('Usuário e senha não conferem.')
