#!/usr/bin/env python3

notas = []
soma = 0

nota = 1
#for nota in range(1,6):
while(True):
	try:
		nota2 = float(input("Digite a nota %d de 5: " %nota))
		if nota2 <= 0 or nota2 >= 10:
			print("Por favor, digite uma nota entre 0 e 10")
			break
		nota+=1
		notas.append(nota2)
		soma+=nota2
	except ValueError:
		print("Digite apenas números")
	if nota == 6:
		break
if nota == 6:
	for nota in range(5):
		print("Nota %d: %.2f" %(nota+1,notas[nota]) )
	print("A Média é %.2f" %(soma/len(notas)) )
else:
	print("Parâmetros incorretos. Favor tentar novamente")
