# Manipulação de texto

Resumo baseado nos métodos de string demonstrados nos exercícios publicados.

## Métodos de classificação

- `isspace()`: verifica se o texto contém apenas espaços em branco.
- `isnumeric()`: verifica se os caracteres são numéricos.
- `isalpha()`: verifica se o texto contém apenas letras.
- `isalnum()`: verifica se há apenas letras e números.
- `isupper()` e `islower()`: verificam o uso de maiúsculas e minúsculas.
- `istitle()`: verifica se o texto está em formato de título.

Esses métodos retornam `True` ou `False` e não alteram o texto original.

## Separação de entradas

O método `split()` separa uma string em partes usando espaços em branco por padrão. Nos exemplos de sorteio simples, isso significa que nomes compostos se dividem em mais de uma palavra. A versão melhorada usa vírgulas como separadores e remove espaços nas extremidades com `strip()`.
