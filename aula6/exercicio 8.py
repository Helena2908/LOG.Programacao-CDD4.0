alunos = []
n = int(input("Quantos alunos possui na instituição?"))
for x in range(n):
    alunos.append(input("Digite o nome do aluno: "))
for y in range(n):
    print(alunos[y], y)


