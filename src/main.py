import argparse
from src.repetipy import obter_duplicatas

def main():
    parser = argparse.ArgumentParser(description="Identifica linhas duplicadas em um arquivo CSV.")
    parser.add_argument("input_csv", help="Caminho do arquivo CSV de entrada")
    parser.add_argument("column_index", type=int, help="Índice da coluna a ser analisada (começa em 0)")
    parser.add_argument("--output_csv", help="Caminho do arquivo CSV de saída (opcional)", default=None)

    args = parser.parse_args()

    try:
        duplicatas = obter_duplicatas(args.input_csv, args.column_index, args.output_csv)

        if duplicatas.empty:
            print("Nenhuma duplicata encontrada!")
        else:
            print("Duplicatas encontradas nas linhas:")
            # Exibindo as duplicatas com a quantidade de vezes que elas aparecem
            print(duplicatas[["Linha Original", duplicatas.columns[args.column_index], "Quantidade Duplicada"]])

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()