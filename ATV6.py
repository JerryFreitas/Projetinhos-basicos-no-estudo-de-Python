bom_dia_nacao = ['Pinheiro', 'Araújo']
jornal_brasileiro = ['Bonner', 'Vasconcelos']

sobrenome = input('Digite o sobrenome de um apresentador: ')


if sobrenome in bom_dia_nacao:
    print('O apresentador(a) faz parte do Bom Dia Nação.')
elif sobrenome in jornal_brasileiro:
    print('O apresentador(a) faz parte do Jornal Brasileiro.')
else:
    print('Apresentador(a) desconhecido(a).')
