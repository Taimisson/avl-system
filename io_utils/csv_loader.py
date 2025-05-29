from datetime import datetime
import csv

from typing import List, Tuple
from models.person import Person
from avl.tree import AVLTree

def load_people(path: str) -> Tuple[List[Person], AVLTree, AVLTree, AVLTree]:
    people: List[Person] = []
    cpf_index, nome_index, nascimento_index = AVLTree(), AVLTree(), AVLTree()

    with open(path, encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=",") # separador 
        next(reader)  # pula a linha de cabeçalho
        for row in reader:
            if len(row) != 5: 
                continue 
            cpf, rg, nome, data, cidade = row 

            person = Person(
                cpf=cpf.zfill(11),
                rg=rg,
                nome=nome.strip(),
                nascimento = datetime.strptime(data.strip(), "%d/%m/%Y").date(),
                cidade=cidade
            )
            people.append(person)
            cpf_index.insert(person.cpf, person)
            nome_index.insert(person.nome.lower(), person)
            nascimento_index.insert(person.nascimento, person)

    return people, cpf_index, nome_index, nascimento_index
            
