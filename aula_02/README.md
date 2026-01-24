# Aula 02 - TypeError, Type Check, Type Conversion, try/except e if

Resumo: nesta aula pratiquei tipos primitivos, conversoes, tratamento de erros e condicionais em Python.
Status: exercicios e desafio executados.

## Conteudo
- Tipos primitivos: int, float, str, bool
- Operacoes basicas e metodos de string
- TypeError e verificacao de tipos (type check)
- Conversao de tipos (type conversion)
- try/except e if/elif/else

## O que eu fiz
- Resolvi todos os exercicios em `aula_02/exercicios.py` usando entradas via input().
- Implementei conversoes, calculos e validacoes de entrada para cada bloco.
- Refatorei o desafio em `aula_02/desafios.py` com funcoes de leitura segura e validacao.

## Exercicios (arquivo)
- `aula_02/exercicios.py`
  - 1-5: inteiros (soma, resto, multiplicacao, divisao inteira, quadrado).
  - 6-10: floats (soma, media, potencia, conversao de temperatura, area do circulo).
  - 11-15: strings (upper, lower, strip, split, concatenacao).
  - 16-20: booleanos e comparacoes.
  - 21-25: try/except e if com validacao e loops.

## Desafio
- `aula_02/desafios.py`
  - Criei `ler_float_nao_negativo` e `ler_nome_nao_vazio` para validar entradas.
  - Evitei valores negativos para salario e bonus.
  - Padronizei o bonus como multiplicador e usei `CONSTANTE_BONUS_ATUAL`.
  - Tratei interrupcoes com `KeyboardInterrupt` e `EOFError`.
  - Imprimi KPI e resumo final para o usuario.
- `aula_02/desafio_gabarito.py`
  - Versao de referencia usada para comparar a solucao.

## Como executar
- `python aula_02/exercicios.py`
- `python aula_02/desafios.py`
- `python aula_02/desafio_gabarito.py` (opcional)

## Observacoes
- Os programas sao interativos e pedem entradas no terminal.
- Para interromper, use Ctrl+C ou EOF (tratado no desafio).


