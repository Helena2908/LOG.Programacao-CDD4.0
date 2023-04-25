alunos = []
cont=0
n = int(input("Quantos alunos possui na instituição? "))
for x in range(n):
    alunos.append(input("Digite o nome do aluno: "))
for y in range(n):
    print(alunos[y], y)
aluno1 = input("Digite o nome de um aluno: ")
for c in range(n):
    if aluno1 == alunos[c]:
        print(c, alunos[c])
    else:
        cont += 1
if cont == n:
    print("Não encontrado!")