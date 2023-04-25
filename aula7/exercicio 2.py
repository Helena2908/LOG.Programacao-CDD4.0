nota = []
soma = 0
cont = 0
for x in range(5):
    nota.append(float(input("Digite a nota do aluno: ")))
for y in range(5):
    soma = soma + nota[y]
media = soma/5
print("A média da turma é: ", media)
for c in range(5):
    if nota[c] >= media:
        cont += 1
print(cont, "Alunos conseguiram conquistar a média da turma")



