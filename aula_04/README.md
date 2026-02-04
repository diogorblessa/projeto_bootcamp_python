# Aula 04 — Estruturas, Funcoes e Leitura de Arquivos

## 📋 Sobre
Esta aula consolida exercicios de logica com listas, dicionarios, funcoes e
validacao de entrada, alem de introduzir leitura de arquivos CSV. O foco e
praticar estruturas basicas do Python e aplicar type hints em um desafio de
entrada e calculo de KPI.

## 🎯 Objetivos de Aprendizado
- Praticar listas, dicionarios e compreensoes.
- Criar funcoes utilitarias para resolver problemas simples.
- Validar entrada de usuario com loops e tratamento de erros.
- Aplicar type hints com o modulo `typing`.
- Ler arquivos CSV com `csv.DictReader`.

## 📁 Estrutura do Projeto
```
aula_04/
|-- desafio.py        # Desafio com validacao e versao tipada
|-- exemplo.csv       # Arquivo CSV de exemplo
|-- exercicios.py     # Exercicios variados (listas, dicts, funcoes)
|-- leitor_arquivos.py# Leitura de CSV com DictReader
`-- README.md
```

## 🛠️ Tecnologias e Ferramentas
- Python 3.11.x: execucao dos scripts.
- Biblioteca padrao `csv`: leitura do arquivo CSV.
- Biblioteca padrao `typing`: type hints no desafio.

## 📦 Pré-requisitos
- Python 3.11.x instalado.
- Conhecimentos basicos de Python (listas, dicionarios, funcoes, loops).

## 🚀 Como Usar
### Instalação
Nao ha dependencias externas. Basta ter o Python instalado.

### Execução
Para executar os exercicios e o desafio:
```bash
python aula_04/exercicios.py
python aula_04/desafio.py
```

Para executar o leitor de CSV a partir do root do repositorio:
```bash
python aula_04/leitor_arquivos.py
```

Se preferir rodar dentro da pasta `aula_04`, ajuste `caminho_arquivo` em
`aula_04/leitor_arquivos.py` para `exemplo.csv`.

## 📚 Conteúdo Real
**`exercicios.py`**: conjunto de tarefas com listas, dicionarios, funcoes,
compreensoes e manipulacao de strings. Inclui entrada de usuario para verificar
se um numero e primo e exemplos de ordenacao e agregacao.

**`desafio.py`**: duas versoes do mesmo fluxo. A primeira valida nome, salario e
bonus e calcula um KPI simples. A segunda reescreve o fluxo com funcoes e type
hints, usando `Tuple` e anotacoes de tipos para deixar o codigo mais claro.

**`leitor_arquivos.py`**: abre `aula_04/exemplo.csv` com `csv.DictReader`,
carrega cada linha em uma lista de dicionarios e imprime os registros.

**`exemplo.csv`**: dados simples com colunas `nome`, `idade` e `cidade` para
teste do leitor.

## 🔗 Conexões com a Formação
- Pré-requisitos: [Aula 01](../aula_01/README.md), [Aula 02](../aula_02/README.md), [Aula 03](../aula_03/README.md)
- Próximos passos: [Aula 06](../aula_06/README.md)

## 📖 Recursos Adicionais
- https://docs.python.org/3/library/csv.html
- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/tutorial/datastructures.html

## 👤 Autor
- Diogo (diogorblessa@yahoo.com)
