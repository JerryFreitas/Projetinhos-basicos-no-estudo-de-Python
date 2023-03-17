#segundosUsuario = int(input("Por favor, entre com o número de segundos que deseja converter:"))

#dias = int(segundosUsuario // 86400)
#horas = int(segundosUsuario //3600)
#minutos = int(segundosUsuario // 60)
#segundos = int(segundosUsuario)

#print(dias,"dias,",horas,"horas",minutos,"minutos",segundos)


# Algoritmo recebe um número e o dispõe nas unidades do tempo com base nos segundos.

totalSegundos = int(input("Por favor, entre com o número de segundos que deseja contar em segundos: "))

dias = totalSegundos // 86400
segundosRestantesDias = totalSegundos % 86400

horas = segundosRestantesDias // 3600
segundosRestantesHoras = segundosRestantesDias % 3600

minutos = segundosRestantesHoras // 60
segundosRestantesMinutos = segundosRestantesHoras % 60

segundos = segundosRestantesMinutos % 60







print(dias,"dias",horas,"horas",minutos,"minutos e",segundos,"segundos.")