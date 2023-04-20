resp = 1
while resp != 6:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número:  "))
    while True:
        resp = int(input(
            "Selecione a operação: \n"
            "1. para soma\n"
            "2. para subtração\n"
            "3. multiplicação\n"
            "4. dibvisão\n"
            "5. para digitar novo numero\n"
            "6. para sair\n"
        ))
        if resp == 1:
            print(num1, "+", num2, "=", num1 + num2)
        elif resp == 2:
            print(num1, "-", num2, "=", num1 - num2)
        elif resp == 3:
            print(num1, "*", num2, "=", num1 * num2)
        elif resp == 4:
            print(num1, "/", num2, "=", num1 / num2)
        elif resp == 5:
            break
        elif resp == 6:
            print("Encerrando o programa.")
            break
