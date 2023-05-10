nome = []
senha = []
cont = 0
for x in range(2):
    nome.append(input("Digite o nome de usuário: "))
    senha.append(input("Digite a senha: "))
usuario = input("Digite o seu usuário: ")
pin = input("Digite sua senha: ")
for y in range(2):
    if usuario == nome[y] and pin == senha[y]:
        print("Login efetuado com sucesso!")
        break
    else:
        cont += 1
if usuario != nome[y] and pin != senha[y]:
    print("Acesso negado!")