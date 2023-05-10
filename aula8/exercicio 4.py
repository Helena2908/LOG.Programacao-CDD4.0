"""Faça um código para ler um vetor de 3 números, Após isso, ler mais um número qualquer,
 calcular e escrever quantas vezes esse número aparece no vetor."""

n = []
cont = 0
for x in range(3):
    n.append(float(input("Digite um número: ")))
numero = float(input("Escolha um número: "))
for y in range(3):
    if numero == n[y]:
        cont += 1
print(cont)