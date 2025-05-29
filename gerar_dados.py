import random
from datetime import datetime, timedelta
import csv

CIDADES = [
    "São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza",
    "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Porto Alegre",
    "Belém", "Goiânia", "Guarulhos", "Campinas", "Natal",
    "Maceió", "João Pessoa", "Teresina", "São Luís", "Campo Grande",
    "Cuiabá", "Aracaju", "Porto Velho", "Boa Vista", "Palmas",
    "Rio Branco", "Macapá", "Vitória", "Florianópolis", "São José dos Campos",
    "Ribeirão Preto", "Uberlândia", "Sorocaba", "Niterói", "São José do Rio Preto",
    "Caxias do Sul", "Juiz de Fora", "Feira de Santana", "Joinville", "Londrina"
]

NOMES = [
    "Ana", "João", "Maria", "Pedro", "Lucas", "Julia", "Gabriel", "Sofia",
    "Matheus", "Isabella", "Rafael", "Laura", "Guilherme", "Beatriz", "Carlos",
    "Mariana", "Daniel", "Carolina", "Bruno", "Amanda", "Eduardo", "Larissa",
    "Felipe", "Camila", "Rodrigo", "Letícia", "Marcos", "Fernanda", "Thiago",
    "Patrícia", "Leonardo", "Juliana", "Gustavo", "Vanessa", "Diego", "Bruna",
    "André", "Natália", "Ricardo", "Marina", "Luciano", "Aline", "Paulo",
    "Claudia", "Roberto", "Tatiana", "Fernando", "Cristina", "Alexandre", "Renata"
]

SOBRENOMES = [
    "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Ferreira",
    "Rodrigues", "Almeida", "Nascimento", "Lima", "Araújo", "Fernandes",
    "Carvalho", "Gomes", "Martins", "Melo", "Cardoso", "Teixeira", "Mendes",
    "Ribeiro", "Alves", "Monteiro", "Moraes", "Cavalcanti", "Dias", "Campos",
    "Barbosa", "Freitas", "Pinto", "Moura", "Castro", "Correia", "Nunes",
    "Moreira", "Medeiros", "Vieira", "Sousa", "Rocha", "Reis", "Lopes",
    "Pires", "Machado", "Ramos", "Gonçalves", "Marques", "Dantas", "Bezerra",
    "Andrade", "Tavares"
]

def gerar_cpf():
    return ''.join(str(random.randint(0, 9)) for _ in range(11))

def gerar_rg():
    return ''.join(str(random.randint(0, 9)) for _ in range(8))

def gerar_nome():
    return f"{random.choice(NOMES)} {random.choice(SOBRENOMES)}"

def gerar_data_nascimento():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2025, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    return (start_date + timedelta(days=random_days)).strftime("%d/%m/%Y")


dados = [["CPF", "RG", "Nome", "Nascimento", "Cidade"]]
for _ in range(200):
    dados.append([
        gerar_cpf(),
        gerar_rg(),
        gerar_nome(),
        gerar_data_nascimento(),
        random.choice(CIDADES)
    ])


with open("data/CSV_de_teste_gerado.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(dados) 