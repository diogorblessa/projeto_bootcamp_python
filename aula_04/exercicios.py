# # 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in lista:
#     print(numero ** 2)

# # 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
# lista = ["Python", "Java", "C++", "JavaScript"]
# lista.remove("C++")
# lista.append("Ruby")
# print(lista)
           

# # 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# livro = {
#     "titulo": "1984",
#     "autor": "George Orwell",
#     "ano": 1948
# }
# for chave, valor in livro.items():
#     # Percorre o dicionario "livro"; items() retorna pares (chave, valor) e, em cada iteracao, "chave" recebe a chave e "valor" o valor correspondente, permitindo acessar ambos no loop.
#     print(f"{chave}: {valor}")

# # 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# def contar_caracteres(s):
#     contagem = {}
#     for caractere in s:
#         # Pega a contagem atual com get (0 se nao existir), soma 1 e grava na chave do caractere.
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem

# print(contar_caracteres("engenharia de dados"))

# # 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
# lista = ["maçã", "banana", "cereja"]
# dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# # Usa sum() para somar: para cada fruta na lista, pega dict[fruta] e acumula.
# preco_total = sum(dict[fruta] for fruta in lista)
# print(f"Preço total: R${preco_total:.2f}")


# # 6. Dada uma lista de emails, remover todos os duplicados.
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# # Remove duplicados convertendo a lista para set (unicos) e depois volta para list.
# emails_unicos = list(set(emails))
# print(emails_unicos)

# # 7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# idades = [22, 15, 30, 17, 18]
# maiores_de_idade = [idade for idade in idades if idade >= 18]
# print(maiores_de_idade)

# # 8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]

# # Ordena a lista pelo campo 'nome'; key recebe uma funcao (lambda) que pega pessoa['nome'] como criterio.
# #Usa lambda quando a funcao e simples e usada uma vez; aqui ela retorna pessoa['nome'] para ordenar.
# #sort() ordena a propria lista (in-place); sorted() criaria uma nova lista e manteria a original.
# nomes_ordenados = pessoas.sort(key=lambda pessoa: pessoa["nome"])
# print(pessoas)

# # 9. Dado um conjunto de números, calcular a média.
# numeros = [10, 20, 30, 40, 50]
# media = sum(numeros) / len(numeros)
# print(f"Média: {media}")

# # 10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = [valor for valor in valores if valor % 2 == 0]
# impares = [valor for valor in valores if valor % 2 != 0]
# print("Pares:", pares)
# print("Ímpares:", impares)

# # 15. Dada uma string, contar a frequência de cada caractere usando um dicionário.
# texto = "engenharia de dados"
# frequencia = {}
# for caractere in texto:
#     frequencia[caractere] = frequencia.get(caractere, 0) + 1
# print(frequencia)

#16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.


#17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.


#18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.


#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.


#20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas