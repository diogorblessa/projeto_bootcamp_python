 # 01. Crie programa que o usuário digita o seu nome e retorna o número de caracteres

print(len(input("Digite seu nome: ")))

# 02. Crie um programa que o usuário digita dois valores e apareça a soma deles
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
print("A soma dos valores é:", num1 + num2)

# 03. Refatore o exercício 01 atribuindo variáveis
nome = input("Digite seu nome: ")
print("O número de caracteres do seu nome é:", len(nome))