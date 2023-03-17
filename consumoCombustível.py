




# Algoritmo calcula a média de consumo de gasolina de um e  



kmIncial = float(input("Qual é a quilometragem incial do veiculo? "))
kmFinal = float(input("Qual é a quilometragem final do veiculo? "))

consumoGasolina = float(input("Qual foi o consumo da gasolina em litros? "))
percurso = kmFinal - kmIncial

media = consumoGasolina / percurso

print("O consumo médio de seu veiculo foi de",media,"quilometros por litros.")