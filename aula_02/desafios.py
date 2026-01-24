### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

CONSTANTE_BONUS_ATUAL = 1000

def ler_float_nao_negativo(prompt):
    while True:
        try:
            valor = float(input(prompt))
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")
            continue
        if valor < 0:
            print("Valor nao pode ser negativo.")
            continue
        return valor

def ler_nome_nao_vazio(prompt):
    while True:
        nome = input(prompt).strip()
        if nome:
            return nome
        print("Nome nao pode ficar vazio.")

try:
    # 1) Solicita ao usuario que digite seu nome
    nome = ler_nome_nao_vazio("Digite seu nome: ")

    # 2) Solicita ao usuario que digite o valor do seu salario
    # Converte a entrada para um numero de ponto flutuante
    salario = ler_float_nao_negativo("Digite seu salario: ")

    # 3) Solicita ao usuario que digite o valor do bonus recebido
    # Converte a entrada para um numero de ponto flutuante
    bonus_multiplicador = ler_float_nao_negativo(
        "Digite o bonus como multiplicador (ex.: 1.5 para 1.5x): "
    )

    # 4) Calcule o valor do bonus final
    valor_do_bonus = CONSTANTE_BONUS_ATUAL + salario * bonus_multiplicador

    # 5) Imprime a mensagem personalizada incluindo o nome do usuario, salario e bonus
    print(f"O KPI e: {valor_do_bonus}")
    print(
        f"Ola {nome}, com um salario de {salario} "
        f"e um bonus de {bonus_multiplicador}x, seu KPI calculado é {valor_do_bonus}."
    )
except (KeyboardInterrupt, EOFError):
    print("\nOperacao interrompida pelo usuario.")
finally:
    print("Programa finalizado.")

# Bonus: Bugs e riscos identificados e correcoes aplicadas:
# - ValueError na conversao de entrada: tratado com try/except e repeticao.
# - Valores negativos aceitos: bloqueados com validacao.
# - Nome vazio: tratado com loop e mensagem de erro.
# - Interrupcao (Ctrl+C/EOF): tratada no try/except com saida segura.
# - Ambiguidade do bonus: prompt indica que e multiplicador.
