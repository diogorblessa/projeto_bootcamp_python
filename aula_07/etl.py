# Importando a biblioteca csv (usada para ler CSV de forma estruturada)
import csv  # disponibiliza DictReader para transformar linhas em dicionarios

path_arquivo = (
    "vendas.csv"  # caminho do arquivo CSV a ser lido (relativo ao diretorio atual)
)


# Funcao para ler csv (encapsula a logica de leitura para reutilizar)
def ler_csv(
    nome_do_arquivo: str,
) -> list[dict]:  # recebe o nome do arquivo e retorna uma lista de dicionarios
    """Le um arquivo CSV e retorna uma lista de dicionarios representando as linhas do arquivo."""
    lista = []  # lista que vai acumular cada linha convertida em dicionario
    with open(
        nome_do_arquivo, mode="r", encoding="utf-8"
    ) as arquivo:  # abre o arquivo com codificacao correta
        leitor = csv.DictReader(
            arquivo
        )  # interpreta o CSV usando a primeira linha como cabecalho
        for linha in leitor:  # percorre cada linha do CSV
            lista.append(linha)  # adiciona a linha (dict) na lista de resultados
    return lista  # devolve a lista completa de linhas


vendas_itens: list[
    dict
]  # anotacao de tipo: lista de dicionarios (nao executa, so documenta)

vendas_itens = ler_csv(path_arquivo)  # chama a funcao usando o caminho definido acima
print(vendas_itens)  # imprime o resultado para verificar o conteudo lido
