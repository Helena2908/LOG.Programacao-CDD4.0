"""forma que eu fiz"""
tipo = input("Informe o tipo de combustível: \nE-etanol \nG-galosina")
litro = float(input("Informe quantos litros?"))
etanol = 4.90
gasolina = 5.80
escolha1 = "E"
escolha2 = "G"
result1 = litro * etanol
result2 = litro * gasolina
if tipo == escolha1:
    print("O preço final do", escolha1, "é", result1)
else:
    print("O preço final do", escolha2, "é", result2)