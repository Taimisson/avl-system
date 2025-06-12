# Sistema de Indexação e Consulta de Pessoas

## Descrição
Este projeto implementa um sistema de indexação e consulta de dados de pessoas utilizando árvores AVL (Adelson-Velsky e Landis). O sistema permite carregar dados de um arquivo CSV e realizar consultas eficientes por CPF, nome e data de nascimento.

## Estrutura do Projeto
```
.
├── avl/                    # Implementação da árvore AVL
│   └── tree.py            # Classe genérica AVLTree
├── cli/                    # Interface de linha de comando
│   └── menu.py            # Menu interativo
├── io_utils/              # Utilitários de entrada/saída
│   └── csv_loader.py      # Carregamento de arquivos CSV
├── models/                # Modelos de dados
│   └── person.py          # Classe Person
├── data/                  # Dados de teste
│   └── CSV_de_teste_gerado.csv
├── gerar_dados.py         # Gerador de dados de teste
├── main.py               # Ponto de entrada da aplicação
└── README.md             # Este arquivo
```

## Requisitos
- Python 3.8 ou superior
- Nenhuma dependência externa necessária

## Como Executar

1. Clone o repositório
2. Execute o programa principal:
```bash
python main.py
```
3. Quando solicitado, forneça o caminho do arquivo CSV (ex: `data/CSV_de_teste_gerado.csv`)

## Funcionalidades

### 1. Carregamento de Dados
- Lê arquivos CSV com dados de pessoas
- Formato esperado: CPF,RG,Nome,Nascimento,Cidade
- Exemplo: `12345678901,543216,João Silva,01/02/1958,Porto Alegre`

### 2. Consultas Disponíveis
- **Busca por CPF**: Encontra uma pessoa específica pelo número do CPF
- **Busca por Nome**: Encontra todas as pessoas cujo nome começa com um prefixo
- **Busca por Data**: Encontra todas as pessoas nascidas em um intervalo de datas

### 3. Indexação
O sistema utiliza três árvores AVL para indexação:
- **Árvore de CPF**: Busca exata por CPF
- **Árvore de Nome**: Busca por prefixo
- **Árvore de Data**: Busca por intervalo

## Implementação Técnica

### Árvore AVL
- Implementação genérica em `avl/tree.py`
- Suporta múltiplas referências por chave
- Operações implementadas:
  - Inserção (O(log n))
  - Busca (O(log n))
  - Remoção (O(log n))
  - Rotações para balanceamento

### Modelo de Dados
- Classe `Person` com os campos:
  - CPF (string)
  - RG (string)
  - Nome (string)
  - Nascimento (date)
  - Cidade (string)

### Interface
- Menu interativo via linha de comando
- Opções numeradas para cada tipo de consulta
- Formatação clara dos resultados

## Geração de Dados de Teste
O projeto inclui um gerador de dados de teste (`gerar_dados.py`) que cria:
- 200 registros aleatórios
- CPFs e RGs únicos
- Nomes e sobrenomes brasileiros
- Datas entre 1950 e 2025
- 40 cidades diferentes

Para gerar novos dados de teste:
```bash
python gerar_dados.py
```

## Autor
Guilherme Lenzi de Oliveira
Taimisson de Carvalho Schardosim

## Data
27/05/2025

## Observações
- O sistema não duplica registros na memória
- As árvores AVL mantêm apenas referências aos objetos
- Todas as consultas são realizadas em tempo O(log n) 