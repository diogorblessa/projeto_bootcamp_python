### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

#Função para verificar a qualidade dos dados
def verificar_qualidade_dados(quantidade, preço):       
    if quantidade > 0 and preço > 0:
        print("Dados válidos")
    else:
        print("Dados inválidos")

# Exemplo de uso
verificar_qualidade_dados(10, 25.5)
verificar_qualidade_dados(-5, 15.0)



### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# - 'Baixa' é menor que 18°C, 
# - 'Normal' é entre 18°C e 26°C, 
# - 'Alta' é maior que 26°C.

# Função para classificar a temperatura
def classificar_temperatura(temperatura):
    if temperatura < 18:
        return 'Baixa'
    elif 18 <= temperatura <= 26:
        return 'Normal'
    else:
        return 'Alta'
    
# Exemplo de uso
print(classificar_temperatura(float(input("Digite a temperatura em °C: "))))



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. 
# Dado um registro de log em formato de dicionário como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

def filtrar_log_por_severidade(log):
    if log['level'] == 'ERROR':
        print(f"Atenção, mensagem de erro: {log['message']}")

# Exemplo de uso
log_exemplo = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
filtrar_log_por_severidade(log_exemplo)




### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# Função para validar dados do usuário
def validar_dados_usuario(idade, email):
    # Valida a faixa de idade primeiro e encerra em caso de erro.
    if not (18 <= idade <= 65):
        print("Erro: Idade inválida. Deve estar entre 18 e 65 anos.")
        return
    # Validacao simples do email: deve ter "@" e ponto no dominio.
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Erro: Email inválido.")
        return
    print("Dados de usuário válidos")

# Exemplo de uso
# Pergunta a idade primeiro para nao pedir email se for invalida.
idade = int(input("Digite a idade do usuario: "))
if 18 <= idade <= 65:
    # So pede o email quando a idade esta no intervalo valido.
    email = input("Digite o email do usuario: ")
    validar_dados_usuario(idade, email)
else:
    # Encerra cedo com uma mensagem de erro clara.
    print("Erro: Idade invalida. Deve estar entre 18 e 65 anos.")



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# Função para detectar anomalias em transações
def detecta_anomalias(transacao, horario_comercial=(9, 18)):
    # Considera suspeita se o valor for alto OU se a hora estiver fora do horario comercial.
    # Checa as duas regras de suspeita: valor acima de 10k ou hora fora do intervalo.
    if transacao['valor'] > 10000 or transacao['hora'] < horario_comercial[0] or transacao['hora'] > horario_comercial[1]:
        print("Transação suspeita detectada.")
    else:
        print("Transação normal.")

# Exemplo de uso
valor = float(input("Digite o valor da transação: "))
hora = int(input("Digite a hora da transação: "))
transacao_exemplo = {'valor': valor, 'hora': hora}
# Chama a função para classificar a transação.
detecta_anomalias(transacao_exemplo)


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# Função para contar palavras em um texto
def contar_palavras(texto):
    # Separa o texto em palavras usando espacos.
    palavras = texto.split()
    # Dicionario para acumular a contagem de cada palavra.
    contagem = {}
    # Percorre cada palavra e normaliza para evitar duplicidade por maiusculas/pontuacao.
    for palavra in palavras:
        # Converte para minusculas e remove pontuacao das extremidades.
        palavra = palavra.lower().strip('.,!?;"\'()[]{}')  # Normaliza a palavra
        # Atualiza a contagem para a palavra atual.
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    # Retorna o dicionario com as contagens.
    return contagem

# Exemplo de uso
# Le um texto do usuario e imprime a contagem de palavras.
texto = input("Digite um texto: ")
contagem = contar_palavras(texto)
print(contagem)



### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# Função para normalizar uma lista de números
def normalizar_dados(numeros):
    min_num = min(numeros)
    max_num = max(numeros)
    # Evita divisao por zero se todos os numeros forem iguais.
    if min_num == max_num:
        return [0.0 for _ in numeros]
    # Aplica a formula de normalizacao para cada numero.
    return [(num - min_num) / (max_num - min_num) for num in numeros]

# Exemplo de uso
numeros = [10, 20, 30, 40, 50]
normalizados = normalizar_dados(numeros)
print(normalizados)


### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando 
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# Função para filtrar dados faltantes
def filtrar_dados_faltantes(usuarios, campo):
    # Filtra os usuarios que estao sem o campo ou com valor vazio.
    return [usuario for usuario in usuarios if not usuario.get(campo)]

# Exemplo de uso
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]
print(filtrar_dados_faltantes(usuarios, "email"))



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Função para extrair números pares
def extrair_numeros_pares(numeros):
    # Retorna uma lista apenas com os numeros pares.
    return [num for num in numeros if num % 2 == 0]

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
print(extrair_numeros_pares(numeros))



### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Função para agregar vendas por categoria
def agregar_vendas_por_categoria(vendas):
    # Dicionario para acumular o total de cada categoria.
    total_por_categoria = {}
    # Percorre cada venda e soma o valor na categoria correspondente.
    for venda in vendas:
        # Se a categoria ja existe, soma; senao, inicializa.
        categoria = venda['categoria']
        valor = venda['valor']
        if categoria in total_por_categoria:
            total_por_categoria[categoria] += valor
        else:
            total_por_categoria[categoria] = valor
    # Retorna o total agregado por categoria.
    return total_por_categoria

# Exemplo de uso
# Lista de vendas com categoria e valor.
vendas = [
    {"categoria": "Eletrônicos", "valor": 1000},
    {"categoria": "Livros", "valor": 200},
    {"categoria": "Eletrônicos", "valor": 500}
]
# Imprime o total por categoria.
print(agregar_vendas_por_categoria(vendas))



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# Função para ler dados até a palavra-chave "sair"
def ler_dados_ate_flag():
    # Loop infinito ate que o usuario digite a palavra de parada.
    while True:
        entrada = input("Digite algo (ou 'sair' para encerrar): ")
        # Verifica a condicao de parada de forma case-insensitive.
        if entrada.lower() == 'sair':
            print("Encerrando a leitura de dados.")
            break
        # Se nao for a palavra-chave, apenas ecoa o que foi digitado.
        print(f"Você digitou: {entrada}")

# Exemplo de uso
# Chama a funcao para iniciar a leitura interativa.
ler_dados_ate_flag()



### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# Função para validar entrada dentro de um intervalo
def validar_entrada_intervalo():
    # Define o intervalo aceitável.
    minimo = 1
    maximo = 100
    # Loop infinito até que a entrada seja válida.
    while True:
        # Tenta converter a entrada para inteiro.
        try:
            entrada = int(input(f"Digite um número entre {minimo} e {maximo}: "))
            # Verifica se o número está dentro do intervalo.
            if minimo <= entrada <= maximo:
                print(f"Número válido: {entrada}")
                # Sai do loop quando a entrada for valida.
                break
            else:
                # Informa que o valor esta fora do intervalo permitido.
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            # Trata entrada n??o num??rica.
            print("Entrada inválida. Digite um número inteiro.")

# Exemplo de uso
# Chama a função para iniciar a validação.
validar_entrada_intervalo()




### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Função para simular consumo de API paginada
def consumir_api_paginada():
    pagina_atual = 1
    paginas_totais = 5  # Simula um total de 5 páginas

    while pagina_atual <= paginas_totais:
        # Simula a obtenção de dados da página atual
        print(f"Processando página {pagina_atual} de {paginas_totais}")
        # Aqui você poderia adicionar lógica para processar os dados da página
        pagina_atual += 1
# Exemplo de uso
consumir_api_paginada()
print("Todas as páginas foram processadas.")    



### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# Função para simular tentativas de conexão
def simular_tentativas_conexao(tentativas_maximas=5, sucesso_em=None):
    # tentativas_maximas define o limite de tentativas
    # sucesso_em define em qual tentativa ocorre sucesso (None = nunca conecta)
    tentativas = 0
    # Flag para indicar se a conexao foi estabelecida
    conectado = False
    # Comeca desconectado; vira True quando a conexao for estabelecida
    # Loop ate conectar ou atingir o limite
    while tentativas < tentativas_maximas and not conectado:
        tentativas += 1
        print(f"Tentativa {tentativas} de {tentativas_maximas}...")
        # Simula sucesso em uma tentativa especifica
        # Se sucesso_em for None, nunca conecta
        conectado = (sucesso_em is not None and tentativas == sucesso_em)
        if conectado:
            print("Conexão bem-sucedida!")
        else:
            print("Falha na conexão.")

    # Se nao conectou, exibe mensagem de limite
    if not conectado:
        print("Número máximo de tentativas atingido. Não foi possível conectar.")

# Exemplo de uso
# Sucesso na 3a tentativa
simular_tentativas_conexao(tentativas_maximas=5, sucesso_em=3)
# Falha em todas as tentativas
simular_tentativas_conexao(tentativas_maximas=5, sucesso_em=None)


### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

# Função para processar dados até encontrar um valor de parada
def processar_dados_ate_parada(itens, valor_parada):
    for item in itens:
        # Verifica se o item atual é o valor de parada
        if item == valor_parada:
            print(f"Valor de parada '{valor_parada}' encontrado. Encerrando o processamento.")
            break
        # Processa o item (aqui apenas imprimimos)
        print(f"Processando item: {item}")

# Exemplo de uso
itens = [1, 2, 3, 4, 'PARAR', 5, 6]
valor_parada = 'PARAR'
processar_dados_ate_parada(itens, valor_parada)