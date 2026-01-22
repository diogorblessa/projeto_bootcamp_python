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
# - Texto com encoding corrompido nas strings/comentarios (ex.: "usuǭrio", "salǭrio", "bǯnus").
# - Saida de erro do PowerShell colada no arquivo (linhas abaixo), causa SyntaxError.
# - Conversao direta com float() sem validacao: entrada invalida gera ValueError.
# - Aceita valores negativos (salario/bonus), KPI pode ficar incoerente.
# - "Valor do bonus" e tratado como multiplicador (salario * bonus), mas o prompt sugere valor absoluto.
# - Constante fixa sem explicacao/regra de negocio clara.


# ===== Versao atualizada (com melhorias) =====
# Comentario: Justificativas das mudancas nesta versao:
# - Validar entradas evita ValueError e melhora a UX.
# - Bloquear negativos evita KPI incoerente.
# - Manter bonus como multiplicador com prompt claro evita ambiguidade.
# - Normalizar nome evita nome vazio e melhora apresentacao.
CONSTANTE_BONUS_ATUAL = 1000  # define a constante base do bonus na versao atualizada

def ler_float_nao_negativo(prompt):  # define funcao para ler float nao negativo com validacao
    while True:  # repete ate obter um valor valido
        try:  # tenta converter a entrada para float
            valor = float(input(prompt))  # converte entrada do usuario em float
        except ValueError:  # trata erro de conversao da entrada
            print("Entrada invalida. Digite um numero valido.")  # avisa que a entrada nao é valida
            continue  # volta ao inicio do loop
        if valor < 0:  # verifica se o valor e negativo
            print("Valor nao pode ser negativo.")  # avisa que valores negativos nao sao aceitos
            continue  # volta ao inicio do loop
        return valor  # retorna o valor validado

nome = input("Digite seu nome: ").strip()  # le o nome e remove espacos laterais
if not nome:  # verifica se o nome ficou vazio
    nome = "Usuario"  # define um nome padrao

salario = ler_float_nao_negativo("Digite seu salario: ")  # le salario com validacao de entrada
bonus_multiplicador = ler_float_nao_negativo("Digite o bonus como multiplicador (ex.: 1.5 para 1.5x): ")  # le bonus como multiplicador para seguir a regra original

valor_do_bonus = CONSTANTE_BONUS_ATUAL + salario * bonus_multiplicador  # calcula o KPI com o bonus multiplicador

print(f"O KPI é: {valor_do_bonus}")  # explica a linha
print(  # inicia a mensagem de saida formatada
    f"Ola {nome}, com um salario de {salario} "  # primeira parte da mensagem com nome e salario
    f"e um bonus de {bonus_multiplicador}x, seu KPI calculado é {valor_do_bonus}."  # segunda parte com bonus e KPI
)  # fecha a chamada de print
