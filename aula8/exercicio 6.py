"""Faça um algoritmo que leia 10 valores do tipo inteiros e armazene em um vetor.
A seguir, o algoritmo deverá informar:
1(todos os números pares que existem no vetor)
2(o menor e o maior valor existente no vetor)
3(quantos dos valores do vetor sao maiores que a media desses valores)"""

valor = []
cont = 0
soma = 0
for x in range(5):
    valor.append(int(input("Digite os valores: ")))
for y in range(5):
    if valor[y] % 2 == 0:
        print("Valores pares: ", valor[y])
maior = valor[0]

for b in range(5):
    if valor[b] > maior:
        maior = valor[b]
print("Maior valor da lista:", maior)
menor = valor[0]
for c in range(5):
    if valor[c] < menor:
        menor = valor[c]
print("Menor valor da lista:", menor)

for a in range(5):
    soma += valor[a]
print("Soma:", soma)
media = soma / 5
print("Média:", media)

for m in range(5):
    if valor[m] > media:
        cont += 1
print("Quantidade de valores maior que a média:", cont)