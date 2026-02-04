# Aula 06 — Padronização de Código com Black, Isort e Flake8

## 📋 Sobre
Esta aula é focada em padronização de código e qualidade. Foram reutilizados
exercícios de aulas anteriores e ajustados para aplicar `black`, `isort` e
`flake8`, além de automatizar a checagem com `pre-commit` e `taskipy`. O objetivo
não é criar novos problemas de negócio, mas consolidar a disciplina de formatação
e lint em um fluxo de trabalho real.

## 🎯 Objetivos de Aprendizado
- Configurar `black`, `isort` e `flake8` com Poetry.
- Entender a função de cada ferramenta no fluxo de qualidade.
- Automatizar o pipeline de formatação e lint com `taskipy`.
- Aplicar hooks com `pre-commit` antes do commit.
- Reutilizar exercícios antigos como base para padronização.

## 📁 Estrutura do Projeto
```
aula_06/
|-- .flake8                  # Config do Flake8 (limite de linha e ignores)
|-- .gitignore               # Ignora .venv e artefatos locais
|-- .pre-commit-config.yaml  # Hooks de qualidade (pre-commit)
|-- .python-version          # Versão alvo do Python (3.11.5)
|-- main.py                  # Exercício reutilizado (temperaturas)
|-- main02.py                # Exercício reutilizado (validação e bônus)
|-- poetry.lock              # Lock de dependências
|-- pyproject.toml           # Configuração do projeto e tools
`-- README.md
```

## 🛠️ Tecnologias e Ferramentas
- Python 3.11.x: execução dos scripts.
- Poetry: gerenciamento de dependências e ambiente virtual.
- Black: formatação automática de código.
- isort: organização de imports (perfil Black).
- Flake8: linting e regras de estilo.
- Taskipy: tasks para rodar o pipeline local.
- pre-commit: hooks de qualidade antes do commit.

## 📦 Pré-requisitos
- Python 3.11.x instalado.
- Poetry instalado.
- Git (para usar pre-commit).
- Conhecimentos básicos de Python.

## 🚀 Como Usar
### Instalação
```bash
cd aula_06
poetry install --no-root
```

### Execução
Para rodar a task de formatação e lint:
```bash
poetry run task format
```

Para rodar os hooks do pre-commit manualmente a partir do root do repo:
```bash
pre-commit run -c aula_06/.pre-commit-config.yaml --all-files
```

## 📚 Conteúdo Real
**Reuso de exercícios**: `main.py` e `main02.py` são exercícios de aulas anteriores
reorganizados para aplicar padronização de estilo. O foco é garantir que o fluxo
de formatação e lint esteja funcionando.

**Configuração de ferramentas**:
o `pyproject.toml` define dependências, `isort` com `profile = "black"` e a task
`format` que executa `isort`, `black` e `flake8`.

**Regras de lint**:
o `.flake8` define `max-line-length = 89` e ignora `E203`, `E701`, `W291` e `E501`
para alinhar com o estilo do Black e reduzir ruído em exercícios antigos.

**Pre-commit**:
o `.pre-commit-config.yaml` configura hooks de limpeza de whitespace, validação
de YAML/TOML e execução de `black`, `isort` e `flake8`.

## 🔗 Conexões com a Formação
- Pré-requisitos: [Aula 01](../aula_01/README.md), [Aula 02](../aula_02/README.md), [Aula 03](../aula_03/README.md), [Aula 04](../aula_04/README.md)
- Próximos passos: aplicar o mesmo fluxo em projetos maiores e integrar CI.

## 📖 Recursos Adicionais
- https://python-poetry.org/docs/
- https://black.readthedocs.io/
- https://pycqa.github.io/isort/
- https://flake8.pycqa.org/
- https://pre-commit.com/
- https://taskipy.readthedocs.io/

## 👤 Autor
- Diogo (diogorblessa@yahoo.com)
