"""Faça um código para ler um valor N qualquer. Após ler dois vetores A e B(de tamanho N cada um)
e depois armazenar em um terceiro vetor Soma a soma dos elementos dos vetores A e B, respeitando
as posições e escrever o vetor Soma"""

n = int(input("Digite um valor para o tamanho do vetor: "))
a = []
b = []
soma = []
for x in range(n):
    a.append(int(input("Digite os números do vetor A: ")))
    b.append(int(input("Digite os números do vetor B: ")))
for y in range(n):
    soma.append(a[y] + b[y])
print(a)
print(b)
print(soma)