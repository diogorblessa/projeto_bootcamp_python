# Integre na solucao anterior um fluxo de while que repita o fluxo ate que o usuario insira as informacoes corretas

# Objetivo: anunciar a seção de inicialização das variaveis de controle do loop
# Inicializa as variaveis para o controle do loop
# Objetivo: iniciar a flag de validacao do nome como falsa para entrar no loop
nome_valido = False
# Objetivo: iniciar a flag de validacao do salario como falsa para entrar no loop
salario_valido = False
# Objetivo: iniciar a flag de validacao do bonus como falsa para entrar no loop
bonus_valido = False

# Objetivo: anunciar a secao de validacao do nome
# Loop para verificar o nome
# Objetivo: repetir a solicitacao do nome ate que ele seja considerado valido
while not nome_valido:
    # Objetivo: proteger a entrada do usuario contra erros de validacao
    try:
        # Objetivo: capturar o nome digitado pelo usuario para validacao
        nome = input("Digite seu nome: ")
        # Objetivo: testar se o nome esta vazio, o que é invalido
        if len(nome) == 0:
            # Objetivo: interromper o fluxo normal e sinalizar erro de validacao
            raise ValueError("O nome nao pode estar vazio.")
        # Objetivo: testar se o nome contem numeros, o que é invalido
        elif any(char.isdigit() for char in nome):
            # Objetivo: interromper o fluxo normal e sinalizar erro de validacao
            raise ValueError("O nome nao deve conter numeros.")
        # Objetivo: tratar o caso em que o nome passou nas validacoes
        else:
            # Objetivo: informar ao usuario que o nome e valido
            print("Nome valido:", nome)
            # Objetivo: marcar a validacao como concluida para sair do loop
            nome_valido = True
    # Objetivo: capturar erros de validacao e informar o motivo ao usuario
    except ValueError as e:
        # Objetivo: exibir a mensagem de erro gerada pela validacao
        print(e)

# Objetivo: anunciar a secao de validacao do salario
# Loop para verificar o salario
# Objetivo: repetir a solicitacao do salario ate que ele seja considerado valido
while not salario_valido:
    # Objetivo: proteger a conversao de entrada e as validacoes
    try:
        # Objetivo: ler o salario e converter para numero de ponto flutuante
        salario = float(input("Digite o valor do seu salario: "))
        # Objetivo: checar se o salario e negativo, o que e invalido
        if salario < 0:
            # Objetivo: orientar o usuario a inserir um valor positivo
            print("Por favor, digite um valor positivo para o salario.")
        # Objetivo: tratar o caso em que o salario passou na validacao
        else:
            # Objetivo: marcar a validacao como concluida para sair do loop
            salario_valido = True
    # Objetivo: capturar erro de conversao quando a entrada nao e numerica
    except ValueError:
        # Objetivo: informar que a entrada foi invalida e pedir novo valor
        print("Entrada invalida para o salario. Por favor, digite um numero.")

# Objetivo: anunciar a secao de validacao do bonus
# Loop para verificar o bonus
# Objetivo: repetir a solicitacao do bonus ate que ele seja considerado valido
while not bonus_valido:
    # Objetivo: proteger a conversao de entrada e as validacoes
    try:
        # Objetivo: ler o bonus e converter para numero de ponto flutuante
        bonus = float(input("Digite o valor do bonus recebido: "))
        # Objetivo: checar se o bonus e negativo, o que e invalido
        if bonus < 0:
            # Objetivo: orientar o usuario a inserir um valor positivo
            print("Por favor, digite um valor positivo para o bonus.")
        # Objetivo: tratar o caso em que o bonus passou na validacao
        else:
            # Objetivo: marcar a validacao como concluida para sair do loop
            bonus_valido = True
    # Objetivo: capturar erro de conversao quando a entrada nao e numerica
    except ValueError:
        # Objetivo: informar que a entrada foi invalida e pedir novo valor
        print("Entrada invalida para o bonus. Por favor, digite um numero.")

# Objetivo: calcular o bonus final usando uma regra simples combinando salario e bonus
bonus_recebido = 1000 + salario * bonus  # Exemplo simples de calculo de bonus

# Objetivo: anunciar a secao de exibicao de resultados ao usuario
# Imprime as informacoes para o usuario
# Objetivo: apresentar nome, salario e bonus final formatados com duas casas decimais
print(f"{nome}, seu salario e R${salario:.2f} e seu bonus final e R${bonus_recebido:.2f}.")
