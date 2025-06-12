"""
Árvore AVL genérica

Autor: Taimisson de Carvalho Schardosim e Guilherme Lenzi   Data: 27/05/2025
"""

from io_utils.csv_loader import load_people
from cli.menu import run_menu

def main():
    path = input("Digite o caminho do arquivo CSV: ").strip()
    people, cpf_index, nome_index, nascimento_index = load_people(path)
    print(f"Arquivo carregado com sucesso! {len(people)} pessoas encontradas.")
    run_menu(people, cpf_index, nome_index, nascimento_index)

if __name__ == "__main__":  
    main()
