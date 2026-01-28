
# import csv

# # Caminho para o arquivo CSV
# caminho_arquivo = 'aula_04/exemplo.csv'

# # Inicializa uma lista vazia para armazenar os dados
# dados = []

# # Usa o gerenciador de contexto `with` para abrir o arquivo
# # with abre e fecha o arquivo automaticamente; caminho_arquivo e o caminho do CSV.
# # mode='r' abre para leitura (texto), le o conteudo e falha se o arquivo nao existir; encoding='utf-8' define a codificacao.
# # r = read: você só vai ler o conteúdo, não pode escrever. Se o arquivo não existir, dá FileNotFoundError.
# with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
#     # Cria um objeto leitor de CSV
#     leitor_csv = csv.DictReader(arquivo)
    
#     # Itera sobre as linhas do arquivo CSV
#     for linha in leitor_csv:
#         # Adiciona cada linha (um dicionário) à lista de dados
#         dados.append(linha)

# # Exibe os dados lidos do arquivo CSV
# for registro in dados:
#     print(registro)

