"""Faça um código para ler 5 nomes de usuários e suas respectivas senhas, e armazenar cada lista
em um array diferente, após completar a digitação, imprimir, nome, senha e posição dos dados no array."""

nome = []
senha = []
for x in range(5):
    nome.append(input("Digite o nome de usuário: "))
    senha.append(input("Digite a senha: "))
for y in range(5):
    print(y, "Usuário:", nome[y], "Senha:", senha[y])