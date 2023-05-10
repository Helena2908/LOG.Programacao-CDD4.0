"""Escreva um algaritmo que solicite ao usuário a entrada de 5 nomes, e que exiba esses nomes.
Após exibir essa lista, o programa deve mostrar também os nomes na ordem inversa"""

nomes = []

for x in range(5):
    nomes.append(input("Digite o nome: "))
print(nomes)
for y in range(4, -1, -1):
    print(nomes[y])