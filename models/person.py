from __future__ import annotations
from dataclasses import dataclass
from datetime import date

@dataclass(slots=True) # isso é para otimizar o desempenho pois é uma classe leve
class Person:
    cpf: str 
    rg: str
    nome: str
    nascimento: date
    cidade: str 

    def __post_init__(self):
        if not isinstance(self.cpf, str) or not isinstance(self.rg, str) or not isinstance(self.nome, str) or not isinstance(self.nascimento, date) or not isinstance(self.cidade, str):
            raise ValueError("Todos os atributos devem ser strings ou datas")
        
    def __str__(self) -> str:
        return (
            f"Nome: {self.nome}\n"
            f"CPF: {self.cpf}\n"
            f"RG: {self.rg}\n"
            f"Nascimento: {self.nascimento:%d/%m/%Y}\n"
            f"Cidade: {self.cidade}\n"
        )
            
            
    
            
