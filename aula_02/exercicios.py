 #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numn1 = int(input("Digite o primeiro número inteiro: "))
numn2 = int(input("Digite o segundo número inteiro: "))
soma = numn1 + numn2
print(f"A soma de {numn1} + {numn2} é {soma}.")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número inteiro: "))
resto = num % 5
print(f"O resto da divisão de {num} por 5 é {resto}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
multiplicacao = num1 * num2
print(f"A multiplicação de {num1} * {num2} é {multiplicacao}.")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
divisao_inteira = num1 // num2
print(f"A divisão inteira de {num1} por {num2} é {divisao_inteira}.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num1 = int(input("Digite um número inteiro: "))
quadrado = num1 ** 2
print(f"O quadrado de {num1} é {quadrado}.")


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"A soma de {num1} + {num2} é {soma}.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
media = (num1 + num2) / 2
print(f"A média de {num1} e {num2} é {media}.")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print(f"A potência de {base} elevado a {expoente} é {potencia}.")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é {temperatura_fahrenheit}.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
from math import pi
raio = float(input("Digite o raio do círculo: "))
area = pi * (raio ** 2)
print(f"A área do círculo é {area:.2f}.")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite uma string: ")
print("String em maiúsculas:", texto.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
print("Nome em minúsculas:", nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
print("Frase sem espaços em branco no início e no final:", frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")
concatenacao = string_1 + string_2
print("Strings concatenadas:", concatenacao)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")
if valor1 == "Banana" and valor2 == "Maçã": 
    resultado = True    
else:
    resultado = False   
print(f"O resultado da operação AND entre {valor1} e {valor2} é {resultado}.")
    

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")
if valor1 == "Banana" or valor2 == "Maçã": 
    resultado = True
else:
    resultado = False   
print(f"O resultado da operação OR entre {valor1} e {valor2} é {resultado}.")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = input("Digite um valor booleano: ")
if valor == "Uva":
    valor_invertido = False
else:
    valor_invertido = True
print(f"O valor invertido é {valor_invertido}.")
    

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 == num2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 != num2:
    print("Os números são diferentes.")
else:
    print("Os números são iguais.")


# #### try-except e if

# 21: Conversor de Temperatura
# Objetivo: converter Celsius para Fahrenheit com validacao de entrada.
# O try principal protege o input; interrupcoes e erros sao tratados sem quebrar o programa.
try:
    # Repete ate o usuario informar um numero valido.
    while True:
        # O try interno valida apenas a conversao da entrada.
        try:
            # Le a entrada do usuario e converte para float.
            temperatura_celsius = float(input("Digite a temperatura em Celsius: "))
            # Aplica a formula de conversao.
            temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
            # Mostra o resultado.
            print(f"A temperatura em Fahrenheit é {temperatura_fahrenheit}.")
            # Encerra o loop quando a conversao der certo.
            break
        # Captura quando a entrada nao pode ser convertida em numero.
        except ValueError:
            # Informa o erro e pede nova entrada.
            print("Por favor, informe um valor numérico para a temperatura.")
# Captura quando o usuario interrompe a execucao (Ctrl+C).
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário.")
# Captura qualquer outro erro inesperado para diagnostico.
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
# O finally sempre executa, com ou sem erro, para finalizar o fluxo.
finally:
    print("Programa finalizado.")


# 22: Verificador de Palíndromo
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

# 23: Calculadora Simples
#O while permite repetir ate uma operacao valida ou o usuario sair.
while True:
    # Flag para controlar o encerramento ao final do ciclo.
    encerrar = False
    # O try trata entradas invalidas sem encerrar o programa.
    try:
        # Le os dois numeros para o calculo.
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        # Le a operacao desejada.
        operacao = input("Escolha a operacao (+, -, *, /) ou 'sair': ")
        # Trata a opcao de sair imediatamente.
        if operacao == "sair":
            print("Calculadora encerrada.")
            encerrar = True
        elif operacao == "+":
            # Soma e mostra o resultado.
            print(f"O resultado de {num1} + {num2} e {num1 + num2}.")
            # Pergunta se deseja outro calculo.
            resposta = input("Deseja fazer outro calculo? (s/n): ").strip().lower()
            # Encerra se nao quiser continuar.
            if resposta != "s":
                encerrar = True
        elif operacao == "-":
            # Subtrai e mostra o resultado.
            print(f"O resultado de {num1} - {num2} e {num1 - num2}.")
            # Pergunta se deseja outro calculo.
            resposta = input("Deseja fazer outro calculo? (s/n): ").strip().lower()
            # Encerra se nao quiser continuar.
            if resposta != "s":
                encerrar = True
        elif operacao == "*":
            # Multiplica e mostra o resultado.
            print(f"O resultado de {num1} * {num2} e {num1 * num2}.")
            # Pergunta se deseja outro calculo.
            resposta = input("Deseja fazer outro calculo? (s/n): ").strip().lower()
            # Encerra se nao quiser continuar.
            if resposta != "s":
                encerrar = True
        elif operacao == "/":
            # Evita divisao por zero.
            if num2 == 0:
                print("Erro: divisao por zero nao e permitida.")
            else:
                # Divide e mostra o resultado.
                print(f"O resultado de {num1} / {num2} e {num1 / num2}.")
                # Pergunta se deseja outro calculo.
                resposta = input("Deseja fazer outro calculo? (s/n): ").strip().lower()
                # Encerra se nao quiser continuar.
                if resposta != "s":
                    encerrar = True
        else:
            # Informa operacao invalida.
            print("Operacao invalida. Use +, -, * ou /.")
    # Captura erro de conversao para numero.
    except ValueError:
        print("Por favor, informe valores numericos.")
    # Trata interrupcao do usuario (Ctrl+C).
    except KeyboardInterrupt:
        print("\nOperacao interrompida pelo usuario.")
        # Confirma se deseja sair ou continuar apos a interrupcao.
        resposta = input("Deseja sair? (s/n): ").strip().lower()
        # Encerra se a resposta for "s".
        if resposta == "s":
            encerrar = True
    finally:
        # Mensagem final quando o programa vai encerrar.
        if encerrar:
            print("Programa finalizado.")
    # Sai do loop quando encerrar for True.
    if encerrar:
        break

# 24: Classificador de Números
while True:
    try:
        numero = float(input("Digite um número (ou 'sair' para encerrar): "))
        if numero > 0:
            print(f"O número {numero} é positivo.")
        elif numero < 0:
            print(f"O número {numero} é negativo.")
        else:
            print("O número é zero.")
    except ValueError:
        entrada = input("Você deseja sair? (s/n): ").strip().lower()
        if entrada == 's':
            print("Programa encerrado.")
            break
        else:
            print("Por favor, insira um número válido.")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        entrada = input("Deseja sair? (s/n): ").strip().lower()
        if entrada == 's':
            print("Programa encerrado.")
            break

# 25: Conversão de Tipo com Validação
numero = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero)
    print(f"O número {numero_inteiro} é um número inteiro.")
except ValueError:
    print("Erro: o valor digitado não é um número inteiro válido.")