import pandas as pd

def obter_duplicatas(csv_file, column_index, output_file=None):
    """Identifica e retorna todas as linhas duplicadas com base em uma coluna específica do CSV."""

    # Carregar o arquivo CSV e pular as linhas problemáticas
    df = pd.read_csv(csv_file, delimiter=';', on_bad_lines='skip')

    # Verificar se o índice da coluna é válido
    if column_index < 0 or column_index >= len(df.columns):
        raise ValueError(f"Índice inválido! O CSV tem {len(df.columns)} colunas.")

    column_name = df.columns[column_index]  # Obtém o nome da coluna pelo índice
    
    # Remover linhas com valores nulos na coluna específica
    df = df.dropna(subset=[column_name])

    # Encontrar todas as duplicatas, incluindo todas as ocorrências
    duplicates = df[df.duplicated(subset=[column_name], keep=False)].copy()

    # Contar as ocorrências de cada valor na coluna
    duplicate_counts = df[column_name].value_counts()

    # Adicionar a posição original da linha no CSV (+2 por causa do índice e do cabeçalho)
    duplicates.insert(0, "Linha Original", duplicates.index + 2)

    # Adicionar a coluna 'Quantidade Duplicada' para contar as duplicações
    duplicates['Quantidade Duplicada'] = duplicates[column_name].map(duplicate_counts)

    # Exibir a contagem das duplicatas
    print(f"\nContagem de duplicatas na coluna '{column_name}':")
    print(duplicate_counts)

    # Garantir que as colunas corretas estão sendo exibidas
    if output_file:
        duplicates.to_csv(output_file, index=False)
        print(f"Duplicatas salvas em: {output_file}")

    return duplicates
