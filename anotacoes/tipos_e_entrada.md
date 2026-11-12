# Tipos básicos e entrada de dados

Anotações organizadas a partir dos exercícios de entrada e conversão de valores.

## `input` retorna texto

Mesmo quando alguém digita números, `input()` retorna uma string. Para fazer cálculos, converta o valor, por exemplo, com `int()` para inteiros ou `float()` para números com parte decimal.

```python
numero = int(input('Digite um número inteiro: '))
```

## Tipos básicos

- `int`: números inteiros, como `7` ou `-4`.
- `float`: números com parte decimal, como `4.5` ou `-3.14`.
- `bool`: `True` ou `False`.
- `str`: texto entre aspas.

A função `type(valor)` mostra o tipo do valor em tempo de execução.

## Conversão para `bool`

Uma string vazia é falsa e uma string não vazia é verdadeira. Portanto, `bool(input(...))` não verifica se a pessoa digitou o número `1`; qualquer texto não vazio resulta em `True`.

## Verificações de texto

Métodos como `isnumeric()`, `isalpha()` e `isalnum()` verificam propriedades da string. Eles não convertem o texto em número. Por exemplo, `isnumeric()` não considera sinal de menos ou separador decimal como parte de uma sequência numérica simples.
