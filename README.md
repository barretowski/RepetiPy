# RepetiPy

**RepetiPy** é uma ferramenta para identificar e analisar duplicatas em arquivos CSV. Ele permite que você identifique quais valores em uma coluna específica se repetem, fornecendo um resumo de contagem de duplicatas, além de possibilitar a exportação dos resultados para um novo arquivo CSV.

## Funcionalidades

- Identifica e marca as linhas duplicadas com base em uma coluna específica de um arquivo CSV.
- Exibe a contagem de duplicatas para os valores presentes na coluna selecionada.
- Permite exportar os resultados em formato CSV para análise posterior.
- Filtra automaticamente as linhas problemáticas durante o processamento (com base no delimitador do CSV).

## Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Para verificar a instalação do Python, execute:

```bash
python --version
```

Além disso, a aplicação usa algumas bibliotecas externas que precisam ser instaladas. Para isso, basta rodar:

```bash
pip install -r requirements.txt
```

## Instalação

1. Clone o repositório para sua máquina:

```bash
git clone https://github.com/seu-usuario/RepetiPy.git
cd RepetiPy
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Usar

### Execução do Script

Para rodar a aplicação, você precisa especificar o caminho para o arquivo CSV de entrada, o índice da coluna a ser analisada e, opcionalmente, o caminho para o arquivo de saída. O comando básico é:

```bash
python -m src.main <input_csv> <column_index> --output_csv <output_csv>
```

#### Parâmetros:

- `input_csv`: Caminho do arquivo CSV de entrada.
- `column_index`: Índice da coluna (começando de 0) que você deseja analisar para duplicatas. Por exemplo, se você deseja analisar a coluna "LINHA DIGITAVEL", passe o índice correspondente.
- `--output_csv`: (opcional) Caminho para salvar o arquivo CSV de saída contendo as duplicatas. Se não fornecido, as duplicatas não serão salvas.

#### Exemplo de Uso

1. Para identificar duplicatas na coluna **"LINHA DIGITAVEL"** (suponha que seja a coluna de índice 6) e salvar os resultados em um arquivo chamado `output.csv`, execute:

```bash
python -m src.main data/extrato.csv 6 --output_csv data/output.csv
```

2. Para apenas visualizar as duplicatas sem salvar em um arquivo:

```bash
python -m src.main data/extrato.csv 6
```

## Explicação dos Resultados

Ao rodar o script, os seguintes resultados serão apresentados:

- **Contagem de duplicatas na coluna especificada**: Exibe quantas vezes cada valor na coluna selecionada aparece.
- **Linha Original**: A posição original das linhas duplicadas no arquivo CSV.
- **Quantidade Duplicada**: Quantas vezes o valor aparece na coluna especificada.

Exemplo de saída:

```
Contagem de duplicatas na coluna 'LINHA DIGITAVEL':
858400000000974900012502901001822069074651000002    2
858200000015124100012500901001822069074655000007    2

Duplicatas encontradas nas linhas:
       Linha Original  LINHA DIGITAVEL  Quantidade Duplicada
36                 38  858400000000974900012502901001822069074651000002                   2
37                 39  858200000015124100012500901001822069074655000007                   2
```

Se o arquivo de saída for especificado com `--output_csv`, ele será salvo no local indicado, contendo todas as duplicatas identificadas.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum bug ou desejar adicionar melhorias, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---