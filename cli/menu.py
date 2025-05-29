from datetime import datetime
from avl.tree import AVLTree
from models.person import Person

def run_menu(pessoas, index_cpf: AVLTree, index_nome: AVLTree, index_nascimento: AVLTree):
    while True:
        print("\n1) CPF\n2) Nome\n3) Nascimento\n0) Sair")
        op = int(input("Escolha uma opção: "))
        if op == 0: break 

        if op == 1:
            try: k = input("CPF (11 dígitos, só números): ").strip().zfill(11)
            except ValueError: print("CPF inválido"); continue 
            indices = index_cpf.search(k)
            if indices:
                for idx in indices:
                    print(pessoas[idx])
            else:
                print("- não encontrado -")
        elif op == 2:
            pref = input("Digite o prefixo do nome: ").lower()
            indices = index_nome.prefix_query(pref)
            if indices:
                for idx in indices:
                    print(pessoas[idx])
            else:
                print("- vazia")
        elif op == 3:
            try:
                d1 = datetime.strptime(input("Digite a data inicial: "), "%d/%m/%Y").date()
                d2 = datetime.strptime(input("Digite a data final: "), "%d/%m/%Y").date()
            except ValueError: print("Data inválida"); continue 
            if d1 > d2: d1, d2 = d2, d1
            indices = index_nascimento.range_query(d1, d2)
            if indices:
                for idx in indices:
                    print(pessoas[idx])
            else:
                print("- vazia")
        else:
            print("Opção inválida")
            
                
