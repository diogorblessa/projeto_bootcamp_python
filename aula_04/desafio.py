## Exercício anterior
# Transforme as variáveis abaixo para utilizarem Type Hinting
# Sem Type Hint:
nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")


# Com Type Hint:
# Desafio com Type Hint: repetir ate dados validos e calcular KPI
# Objetivo: importar Tuple do modulo typing para anotar retornos com varios valores
from typing import Tuple

# Objetivo: definir uma funcao tipada; "-> str" explica que a funcao retorna texto
def ler_nome_valido() -> str:
    # Objetivo: repetir a leitura ate que o nome passe na validacao
    while True:
        # Objetivo: ler a entrada do usuario; ": str" explicita o tipo esperado
        nome_lido: str = input("Digite seu nome: ")
        # Objetivo: bloquear nome vazio para evitar dado invalido
        if len(nome_lido) == 0:
            # Objetivo: informar o motivo da falha ao usuario
            print("O nome nao pode estar vazio.")
            # Objetivo: voltar ao inicio do loop para pedir novamente
            continue
        # Objetivo: bloquear nomes com numeros usando uma verificacao por caractere
        # Objetivo: any() retorna True se pelo menos um item for True
        # Objetivo: char.isdigit() verifica se o caractere e um numero
        # Objetivo: "for char in nome_lido" percorre cada caractere do texto
        if any(char.isdigit() for char in nome_lido):
            # Objetivo: informar o motivo da falha ao usuario
            print("O nome nao deve conter numeros.")
            # Objetivo: voltar ao inicio do loop para pedir novamente
            continue
        # Objetivo: retornar o nome quando passou em todas as validacoes
        return nome_lido

# Objetivo: definir uma funcao tipada; "mensagem: str" indica o tipo do parametro
def ler_float_nao_negativo(mensagem: str) -> float:
    # Objetivo: repetir a leitura ate obter um numero valido
    while True:
        # Objetivo: proteger a conversao para float
        try:
            # Objetivo: converter a entrada em float e tipar o valor
            valor: float = float(input(mensagem))
            # Objetivo: impedir valores negativos
            if valor < 0:
                # Objetivo: orientar o usuario a inserir um valor positivo
                print("Por favor, digite um valor positivo.")
                # Objetivo: voltar ao inicio do loop para pedir novamente
                continue
            # Objetivo: retornar o valor valido
            return valor
        # Objetivo: tratar entradas nao numericas
        except ValueError:
            # Objetivo: informar erro e solicitar nova tentativa
            print("Entrada invalida. Por favor, digite um numero.")

# Objetivo: definir a regra de calculo do KPI com tipos explicitos nos parametros e retorno
def calcular_kpi(salario_valor: float, bonus_valor: float) -> float:
    # Objetivo: calcular o KPI conforme a regra simples do desafio
    return 1000 + salario_valor * bonus_valor

# Objetivo: definir uma funcao tipada que retorna uma tupla (nome, salario, bonus)
def coletar_dados() -> Tuple[str, float, float]:
    # Objetivo: ler e validar nome usando a funcao dedicada
    nome: str = ler_nome_valido()
    # Objetivo: ler e validar salario com uma mensagem especifica
    salario: float = ler_float_nao_negativo("Digite o valor do seu salario: ")
    # Objetivo: ler e validar bonus com uma mensagem especifica
    bonus: float = ler_float_nao_negativo("Digite o valor do bonus recebido: ")
    # Objetivo: devolver os dados em uma tupla tipada
    return nome, salario, bonus

# Objetivo: declarar as variaveis com type hint antes da atribuicao
nome: str
# Objetivo: declarar o salario com type hint para clareza
salario: float
# Objetivo: declarar o bonus com type hint para clareza
bonus: float
# Objetivo: coletar os dados e desempacotar a tupla em variaveis tipadas
nome, salario, bonus = coletar_dados()
# Objetivo: calcular o bonus final com base nos dados validados
bonus_recebido: float = calcular_kpi(salario, bonus)

# Objetivo: exibir o resultado formatado para o usuario
print(
    f"{nome}, seu salario e R${salario:.2f} e seu bonus final e R${bonus_recebido:.2f}."
)
idade: int = 31
altura: float = 1.74
nome: str = "Diogo"
is_estudante: bool = True


