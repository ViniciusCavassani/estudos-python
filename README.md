# Estudos de Python

Repositório de exercícios feitos durante meus estudos iniciais de Python. Aqui organizo exemplos de aula e desafios de lógica em pequenos programas de terminal.

O objetivo é registrar a aprendizagem e praticar os fundamentos. Estes arquivos são exercícios didáticos: não são aplicações de produção e nem todos tratam entradas inválidas.

## Conteúdo

### Primeiros passos

| Arquivo | Prática |
|---|---|
| [`01_ola_mundo.py`](exercicios/primeiros_passos/01_ola_mundo.py) | Saída de texto com `print` |
| [`02_saudacao.py`](exercicios/primeiros_passos/02_saudacao.py) | Entrada de texto e formatação |
| [`03_classificando_texto.py`](exercicios/primeiros_passos/03_classificando_texto.py) | Métodos básicos de strings |

### Desafios

| Arquivo | Prática |
|---|---|
| [`003_soma.py`](desafios/003_soma.py) | Entrada de inteiros e soma |
| [`004_propriedades_de_texto.py`](desafios/004_propriedades_de_texto.py) | Classificação de strings |
| [`005_antecessor_sucessor.py`](desafios/005_antecessor_sucessor.py) | Operações com inteiros |
| [`006_dobro_triplo_raiz.py`](desafios/006_dobro_triplo_raiz.py) | Operações com números reais |
| [`007_media_de_notas.py`](desafios/007_media_de_notas.py) | Média aritmética |
| [`008_conversao_de_medidas.py`](desafios/008_conversao_de_medidas.py) | Conversão de metros |
| [`009_tabuada.py`](desafios/009_tabuada.py) | Multiplicação e saída formatada |
| [`010_conversao_de_moeda.py`](desafios/010_conversao_de_moeda.py) | Divisão com taxa fixa de exemplo |
| [`011_area_e_tinta.py`](desafios/011_area_e_tinta.py) | Área e proporção |
| [`012_desconto.py`](desafios/012_desconto.py) | Cálculo de porcentagem |
| [`013_aumento_salarial.py`](desafios/013_aumento_salarial.py) | Cálculo de porcentagem |
| [`014_celsius_fahrenheit.py`](desafios/014_celsius_fahrenheit.py) | Conversão de temperatura |
| [`015_aluguel_de_carro.py`](desafios/015_aluguel_de_carro.py) | Cálculo a partir de duas tarifas |
| [`016_parte_inteira.py`](desafios/016_parte_inteira.py) | Uso de `math.trunc` |
| [`017_hipotenusa.py`](desafios/017_hipotenusa.py) | Uso de `math.hypot` |
| [`018_trigonometria.py`](desafios/018_trigonometria.py) | Seno, cosseno e tangente |
| [`019_sorteio_de_nome.py`](desafios/019_sorteio_de_nome.py) | Escolha aleatória |
| [`020_ordem_de_apresentacao.py`](desafios/020_ordem_de_apresentacao.py) | Embaralhamento de uma lista |

## Como executar

É necessário ter Python 3 instalado. No terminal, entre na pasta do repositório e execute um arquivo, por exemplo:

```bash
python desafios/003_soma.py
```

No Windows, também pode ser necessário usar `py` no lugar de `python`:

```bash
py desafios/003_soma.py
```

Os programas são independentes; execute um arquivo por vez.

## Observações sobre os exercícios

- A conversão de moeda usa uma taxa fixa de `5.50` apenas como valor didático. Não representa uma cotação atual.
- O exercício de raiz quadrada espera um valor não negativo.
- Os sorteios esperam que sejam informados nomes separados por espaços; nomes compostos não são tratados como uma única entrada.
- Alguns exercícios podem ser simplificados ou ampliados conforme avanço nos estudos.

## Organização

- `exercicios/primeiros_passos/`: exemplos introdutórios.
- `desafios/`: soluções de desafios numerados.

Este repositório é um registro de estudos e será atualizado conforme eu aprender novos conceitos.
