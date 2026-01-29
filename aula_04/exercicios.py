# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista:
    print(numero ** 2)

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)
           

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    "titulo": "1984",
    "autor": "George Orwell",
    "ano": 1948
}
for chave, valor in livro.items():
    # Percorre o dicionario "livro"; items() retorna pares (chave, valor) e, em cada iteracao, "chave" recebe a chave e "valor" o valor correspondente, permitindo acessar ambos no loop.
    print(f"{chave}: {valor}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        # Pega a contagem atual com get (0 se nao existir), soma 1 e grava na chave do caractere.
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista = ["maçã", "banana", "cereja"]
dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# Usa sum() para somar: para cada fruta na lista, pega dict[fruta] e acumula.
preco_total = sum(dict[fruta] for fruta in lista)
print(f"Preço total: R${preco_total:.2f}")


# 6. Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# Remove duplicados convertendo a lista para set (unicos) e depois volta para list.
emails_unicos = list(set(emails))
print(emails_unicos)

# 7. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]
maiores_de_idade = [idade for idade in idades if idade >= 18]
print(maiores_de_idade)

# 8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

# Ordena a lista pelo campo 'nome'; key recebe uma funcao (lambda) que pega pessoa['nome'] como criterio.
#Usa lambda quando a funcao e simples e usada uma vez; aqui ela retorna pessoa['nome'] para ordenar.
#sort() ordena a propria lista (in-place); sorted() criaria uma nova lista e manteria a original.
nomes_ordenados = pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)

# 9. Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)
print(f"Média: {media}")

# 10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]
print("Pares:", pares)
print("Ímpares:", impares)

# 15. Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
frequencia = {}
for caractere in texto:
    frequencia[caractere] = frequencia.get(caractere, 0) + 1
print(frequencia)

#16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
#Função que soma todos os números em uma lista.
def soma_numeros(lista):
    return sum(lista)

# Bloco principal:
lista = [1, 2, 3, 4, 5]
resultado = soma_numeros(lista)
print(f"A soma dos números na lista é: {resultado}")

#17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def define_primo(numero):
    if numero <= 1:
        return False
    # Explicacao do "for i in range(2, int(numero**0.5) + 1):"
    # for -> inicia um loop que percorre uma sequencia
    # i -> variavel iteradora que recebe cada valor do range
    # range(2, ... ) -> gera inteiros a partir de 2 (menor divisor possivel)
    # int(numero**0.5) -> calcula a raiz quadrada de numero e converte para inteiro
    # + 1 -> o fim do range é exclusivo; soma 1 para incluir a raiz, se necessario
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
print(f"O número {numero} é primo? {define_primo(numero)}")

#18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def inverte_string(s):
    return s[::-1]

# Bloco principal:
string = "engenharia de dados"
string_invertida = inverte_string(string)
print(f"String original: {string_invertida}")

#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def combina_pares(lista, numero):
    # Cria a lista onde os pares válidos serão armazenados.
    pares = []
    # i percorre todas as posicoes possiveis da lista (0 ate o ultimo indice).
    # Em cada iteracao, lista[i] é o primeiro elemento do par.
    for i in range(len(lista)):
        # j comeca em i + 1 para pegar apenas elementos depois de i.
        # Isso evita repetir pares invertidos (ex.: nao pega (2,5) e depois (5,2)).
        for j in range(i + 1, len(lista)):
            # Soma os dois elementos e compara com o numero alvo.
            if lista[i] + lista[j] == numero:
                # Guarda o par como uma tupla.
                pares.append((lista[i], lista[j]))
    return pares

# Bloco principal:
numeros = [1, 2, 3, 4, 5]
alvo = 5
resultado = combina_pares(numeros, alvo)
print(f"Pares que somam {alvo}: {resultado}")


#20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def chaves_ordenadas(dicionario):
    # keys() devolve as chaves do dicionario; sorted() ordena essas chaves e retorna uma nova lista.
    return sorted(dicionario.keys())

# Bloco principal:
meu_dicionario = {"banana": 3, "maçã": 5, "laranja": 2, "abacaxi": 4}
chaves = chaves_ordenadas(meu_dicionario)
print(f"Chaves ordenadas: {chaves}")

# Se eu quisesse ordenar pelos valores, poderia usar:
def chaves_ordenadas(dicionario):
    # keys() devolve as chaves do dicionario; sorted() ordena essas chaves e retorna uma nova lista.
    return sorted(dicionario.items(), key=lambda item: item[1])

# Bloco principal:
meu_dicionario = {"banana": 3, "maçã": 5, "laranja": 2, "abacaxi": 4}
chaves = chaves_ordenadas(meu_dicionario)
print(f"Chaves ordenadas: {chaves}")
