# Estudos de Python

Repositório de exercícios e anotações feitos durante meus estudos iniciais de Python. Os arquivos registram práticas de aula e desafios de lógica em pequenos programas de terminal.

O objetivo é praticar fundamentos e acompanhar a evolução do código. Estes são exercícios didáticos, não aplicações de produção. Os arquivos originais foram organizados em cópias revisadas; não incluí configurações do PyCharm, arquivos vazios ou o áudio do exercício com Pygame.

## Conteúdo

### Primeiros passos

| Arquivo | Prática |
|---|---|
| [`01_ola_mundo.py`](exercicios/primeiros_passos/01_ola_mundo.py) | Saída de texto com `print` |
| [`02_saudacao.py`](exercicios/primeiros_passos/02_saudacao.py) | Entrada de texto e formatação |
| [`03_classificando_texto.py`](exercicios/primeiros_passos/03_classificando_texto.py) | Métodos básicos de strings |
| [`04_soma_de_inteiros.py`](exercicios/primeiros_passos/04_soma_de_inteiros.py) | Conversão para inteiro e soma |

### Exercícios de aula

| Arquivo | Prática |
|---|---|
| [`01_soma_basica.py`](exercicios/operacoes/01_soma_basica.py) | Leitura e soma de dois inteiros |
| [`02_operacoes_aritmeticas.py`](exercicios/operacoes/02_operacoes_aritmeticas.py) | Soma, produto, divisões e potência |
| [`03_raiz_quadrada.py`](exercicios/operacoes/03_raiz_quadrada.py) | Uso de `math.sqrt` |
| [`04_numero_aleatorio.py`](exercicios/operacoes/04_numero_aleatorio.py) | Uso de `random.randint` |

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
| [`019_sorteio_de_nome.py`](desafios/019_sorteio_de_nome.py) | Escolha aleatória de um nome |
| [`020_ordem_de_apresentacao.py`](desafios/020_ordem_de_apresentacao.py) | Embaralhamento de uma lista |

### Versões melhoradas

Os arquivos nesta pasta ampliam exercícios anteriores com validação e condicionais. Essas melhorias acrescentam conceitos além dos exemplos iniciais.

| Arquivo | O que foi ampliado |
|---|---|
| [`01_operacoes_com_divisor_zero.py`](versoes_melhoradas/01_operacoes_com_divisor_zero.py) | Evita calcular divisões quando o segundo valor é zero |
| [`02_raiz_com_validacao.py`](versoes_melhoradas/02_raiz_com_validacao.py) | Informa quando a entrada é negativa |
| [`03_sorteio_com_lista_validada.py`](versoes_melhoradas/03_sorteio_com_lista_validada.py) | Filtra entradas vazias antes do sorteio |
| [`04_conversao_com_taxa_informada.py`](versoes_melhoradas/04_conversao_com_taxa_informada.py) | Solicita a taxa usada no cálculo em vez de fixá-la no código |

### Anotações

- [`tipos_e_entrada.md`](anotacoes/tipos_e_entrada.md): `input`, conversão de tipos e verificações de texto.
- [`operadores.md`](anotacoes/operadores.md): operadores e precedência.
- [`modulos.md`](anotacoes/modulos.md): exemplos com `math` e `random`.
- [`manipulacao_de_texto.md`](anotacoes/manipulacao_de_texto.md): métodos de strings usados nos exercícios.

## Exemplos de uso

Os exemplos abaixo ilustram o formato de interação esperado; não são resultados de execução registrada.

### Saudação

```text
Digite seu nome: Ana
Prazer em te conhecer, Ana!
```

### Soma de inteiros

```text
Digite um valor: 7
Digite outro valor: 5
A soma entre 7 e 5 é igual a 12.
```

### Hipotenusa

```text
Digite o valor do cateto oposto: 3
Digite o valor do cateto adjacente: 4
A hipotenusa calculada é 5.00.
```

## Como executar

É necessário ter Python 3 instalado. No terminal, entre na pasta do repositório e execute um arquivo, por exemplo:

```bash
python exercicios/operacoes/02_operacoes_aritmeticas.py
```

No Windows, também pode ser necessário usar `py` no lugar de `python`:

```bash
py desafios/003_soma.py
```

Os programas são independentes; execute um arquivo por vez. Os exemplos deste repositório usam a biblioteca padrão do Python e não exigem instalação de pacotes externos.

## Observações

- A conversão de moeda em `desafios/010_conversao_de_moeda.py` usa `5.50` somente como valor didático, não como cotação atual.
- O exercício original de raiz quadrada espera um valor não negativo; a validação está na versão melhorada.
- O sorteio simples espera nomes separados por espaços; nomes compostos são tratados como partes separadas. A versão melhorada usa nomes separados por vírgulas.
- O arquivo de áudio do exercício com Pygame não foi incluído porque os direitos de distribuição não foram confirmados.
- Os arquivos são registros de aprendizagem e podem ser ampliados conforme eu estudar novos conceitos.

## Organização

- `exercicios/`: exercícios de introdução e de aula.
- `desafios/`: desafios numerados.
- `versoes_melhoradas/`: revisões que acrescentam validação.
- `anotacoes/`: resumos reorganizados a partir dos conceitos demonstrados nos exercícios.
