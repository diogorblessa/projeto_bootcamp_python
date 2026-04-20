# BOOTCAMP_PYTHON

## 📋 Sobre
Este repositório reúne exercícios e desafios do bootcamp de Python da Jornada de Dados. O conteúdo atual está organizado por aulas independentes, com foco em lógica básica, validação de entrada, estruturas de dados, leitura de arquivos CSV e padronização de código.

O material tem perfil educacional e progressivo: as primeiras aulas concentram scripts interativos executados no terminal, enquanto as aulas mais recentes introduzem leitura de arquivos e ferramentas de qualidade de código. A documentação abaixo reflete o estado real do repositório em 20 de abril de 2026.

## 🎯 Objetivos de Aprendizado
- Praticar `print()`, `input()`, variáveis e conversão de tipos.
- Aplicar `if`, `elif`, `else`, `while`, `for`, listas e dicionários.
- Validar entradas do usuário com `try/except`.
- Organizar código em funções com type hints.
- Ler arquivos CSV com `csv.DictReader`.
- Entender um fluxo básico de padronização com `black`, `isort`, `flake8`, `pre-commit` e `taskipy`.

## 📁 Estrutura do Projeto
```text
bootcamp_python/
|-- README.md
|-- .gitignore
|-- aula_01/
|   |-- README.md
|   |-- main.py              # Exercícios iniciais com input, print e soma
|   `-- kpi.py               # Cálculo de KPI/bonus com e sem validação
|-- aula_02/
|   |-- README.md
|   |-- exercicios.py        # Tipos primitivos, strings, booleanos, try/except e if
|   |-- desafios.py          # Refatoração do desafio com validação de entrada
|   `-- desafio_gabarito.py  # Versão de referência
|-- aula_03/
|   |-- README.md
|   |-- exercicios.py        # Funções com condicionais, listas, dicionários e loops
|   |-- desafio.py           # Fluxo com while para validar nome, salário e bonus
|   `-- desafio_gabarito.py  # Versão de referência
|-- aula_04/
|   |-- README.md
|   |-- exercicios.py        # Listas, dicionários, funções e número primo
|   |-- desafio.py           # Desafio com type hints
|   |-- leitor_arquivos.py   # Leitura de CSV com DictReader
|   `-- exemplo.csv          # Arquivo de exemplo para leitura
|-- aula_06/
|   |-- README.md
|   |-- pyproject.toml       # Dependências e task de formatação/lint
|   |-- poetry.lock
|   |-- .flake8
|   |-- .pre-commit-config.yaml
|   |-- .python-version
|   |-- .gitignore
|   |-- main.py              # Processamento de temperaturas por estação
|   `-- main02.py            # Script interativo reutilizado para validação
`-- aula_07/
    |-- README.md            # Arquivo presente, atualmente vazio
    |-- etl.py               # Leitura simples de vendas.csv
    `-- vendas.csv           # Base CSV usada no script
```

## 🛠️ Tecnologias e Ferramentas
- Python: linguagem usada em todos os scripts do repositório.
- Biblioteca padrão `csv`: leitura estruturada de `aula_04/exemplo.csv` e `aula_07/vendas.csv`.
- Biblioteca padrão `typing`: usada em `aula_04/desafio.py`.
- Biblioteca padrão `collections`: `defaultdict` em `aula_06/main.py`.
- Biblioteca padrão `pathlib`: manipulação de caminho em `aula_06/main.py`.
- Poetry: gerenciamento de dependências em `aula_06`.
- Black: formatação automática em `aula_06`.
- isort: organização de imports em `aula_06`.
- Flake8: lint em `aula_06`.
- pre-commit: hooks locais de qualidade em `aula_06`.
- Taskipy: task `format` configurada em `aula_06/pyproject.toml`.

## 📦 Pré-requisitos
- Python 3 instalado e acessível no terminal.
- Para `aula_06`: Poetry instalado.
- Conhecimentos básicos de terminal.
- Noções iniciais de Python ajudam, mas as aulas 01 a 04 foram escritas para prática introdutória.

## 🚀 Como Usar
### Instalação
Para as aulas 01, 02, 03, 04 e 07, não há dependências externas:

```bash
git clone <URL_DO_REPOSITORIO>
cd bootcamp_python
```

Para a `aula_06`, instale as dependências do projeto Poetry:

```bash
cd aula_06
poetry install --no-root
cd ..
```

### Execução
Exemplos de execução a partir da raiz do repositório:

```bash
python aula_01/main.py
python aula_01/kpi.py
python aula_02/exercicios.py
python aula_02/desafios.py
python aula_03/exercicios.py
python aula_03/desafio.py
python aula_04/exercicios.py
python aula_04/desafio.py
python aula_04/leitor_arquivos.py
```

Para a `aula_07`, execute o script de dentro da própria pasta, porque `etl.py` usa o caminho relativo `vendas.csv`:

```bash
cd aula_07
python etl.py
```

Para a `aula_06`, os comandos dependem do ambiente Poetry:

```bash
cd aula_06
poetry run task format
pre-commit run --all-files
```

Observações importantes:
- Os scripts das aulas 01 a 04 e `aula_06/main02.py` são interativos e pedem entrada no terminal.
- `aula_06/main.py` referencia `data/measurements.txt`, mas esse arquivo não está versionado no repositório atual. Portanto, ele não pode ser executado com sucesso sem adicionar a base esperada.
- Os scripts `aula_04/leitor_arquivos.py` e `aula_07/etl.py` foram validados com um interpretador Python local explícito no ambiente.

## 📚 Conteúdo Real
### Aula 01
`aula_01/main.py` contém três exercícios básicos: contar caracteres do nome, somar dois inteiros e refatorar a leitura do nome usando variável. `aula_01/kpi.py` calcula um KPI com a fórmula `1000 + salario * bonus`, primeiro em uma versão direta e depois em uma versão com validação de número não negativo.

### Aula 02
`aula_02/exercicios.py` agrupa vários exercícios sequenciais sobre inteiros, floats, strings, comparações, tratamento de erro, palíndromo, calculadora simples, classificador de números e conversão com validação. `aula_02/desafios.py` refatora o desafio do KPI com funções auxiliares para nome não vazio e float não negativo, além de tratar `KeyboardInterrupt` e `EOFError`.

### Aula 03
`aula_03/exercicios.py` organiza a prática em funções como `verificar_qualidade_dados`, `classificar_temperatura`, `filtrar_log_por_severidade`, `validar_dados_usuario`, `agregar_vendas_por_categoria` e outros fluxos com loops e controle de parada. `aula_03/desafio.py` repete a coleta de nome, salário e bonus até obter entradas válidas.

### Aula 04
`aula_04/exercicios.py` mistura exercícios diretos e funções como `contar_caracteres`, `soma_numeros`, `define_primo`, `inverte_string` e `combina_pares`. `aula_04/desafio.py` reaproveita o problema do KPI e inclui uma segunda versão com type hints e funções tipadas. `aula_04/leitor_arquivos.py` lê `aula_04/exemplo.csv` com `csv.DictReader` e imprime cada registro.

### Aula 06
`aula_06` é um módulo voltado a padronização de código. `pyproject.toml` declara `black`, `isort`, `taskipy` e `pre-commit`, enquanto `.pre-commit-config.yaml` adiciona hooks de limpeza, validação de YAML/TOML e lint. A task `format` definida hoje roda `isort`, `black` e `flake8` apenas sobre `main.py`. `main02.py` existe na pasta, mas não entra nessa task.

### Aula 07
`aula_07/etl.py` implementa uma função `ler_csv(nome_do_arquivo: str) -> list[dict]`, lê `vendas.csv` com `csv.DictReader` e imprime a lista de vendas carregada. O arquivo `README.md` da aula existe, mas está vazio neste momento.

## 🔗 Conexões com a Formação
- Pré-requisitos: as aulas foram construídas em sequência lógica, começando em [aula_01](./aula_01/README.md) e avançando por [aula_02](./aula_02/README.md), [aula_03](./aula_03/README.md) e [aula_04](./aula_04/README.md).
- Próximos passos: [aula_06](./aula_06/README.md) introduz qualidade de código; [aula_07](./aula_07/README.md) começa a trabalhar leitura de dados tabulares.
- Observação de estrutura: não há pasta `aula_05` versionada no estado atual do repositório.

## 📖 Recursos Adicionais
- Python Tutorial: https://docs.python.org/3/tutorial/
- CSV no Python: https://docs.python.org/3/library/csv.html
- Typing no Python: https://docs.python.org/3/library/typing.html
- Poetry: https://python-poetry.org/docs/
- Black: https://black.readthedocs.io/
- isort: https://pycqa.github.io/isort/
- Flake8: https://flake8.pycqa.org/
- pre-commit: https://pre-commit.com/
- GitHub Flavored Markdown: https://github.github.com/gfm/

## 👤 Autor
- Diogo
- E-mail: diogorblessa@yahoo.com
