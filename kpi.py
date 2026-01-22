CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
# Armazena o nome em uma variável
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(f"O KPI é: {valor_do_bonus}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, com um salário de {salario} e um bônus de {bonus}, seu KPI calculado é {valor_do_bonus}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?