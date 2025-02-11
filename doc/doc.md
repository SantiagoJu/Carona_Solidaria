# Projeto Sistema de Caronas UnB
> Disciplina: Algoritmos e Programação de Computadores (APC)

## 1. Descrição do Projeto
O Sistema de Caronas UnB é uma aplicação desenvolvida em Python que visa facilitar o compartilhamento de caronas entre membros da comunidade universitária. O sistema permite que usuários cadastrem ofertas de caronas e que outros usuários possam buscar por caronas disponíveis de acordo com suas necessidades.

## 2. Estrutura do Projeto

### 2.1 Arquivos do Projeto
```
projeto/
├── main.py           # Arquivo principal com o menu e lógica do programa
├── src/
│   ├── database.py   # Gerenciamento do banco de dados
│   └── utils.py      # Funções auxiliares
└── data/
    ├── dim_user.parquet    # Tabela dimensão de usuários
    └── fact_ride.parquet   # Tabela fatos de caronas
```

### 2.2 Bibliotecas Utilizadas
- `pandas`: Manipulação e análise de dados
- `pyarrow`: Suporte para arquivos .parquet


## 3. Estrutura do Código

## 3.1 Funcionalidades

### 1. Cadastro de Usuário (Opção 1)
- Coleta dados do usuário:
  - Nome
  - Email
  - Telefone
  - Região administrativa
- Gera automaticamente:
  - ID único
  - Chave privada
- Armazena dados na tabela dimensão (dim_user.parquet)

### 2. Cadastro de Oferta de Carona (Opção 2)
- Autenticação via chave privada
- Coleta dados da carona:
  - Local de origem
  - Local de destino (UNB ou outra localidade)
  - Data e horário
- Armazena dados na tabela fatos (fact_ride.parquet)

### 3. Busca de Carona (Opção 3)
- Permite buscar caronas por:
  - Local de origem
  - Local de destino
  - Intervalo de data/horário
- Exibe caronas disponíveis que atendem aos critérios

### 4. Busca de Informações de Contato (Opção 4)
- Busca por ID do usuário
- Exibe informações de contato do ofertante:
  - Nome
  - Telefone


### 3.2 Classe DataBase (database.py)
A classe `DataBase` é responsável pelo gerenciamento do banco de dados do sistema.

#### Métodos:
1. `exist_database(path)`:
   - Verifica a existência dos arquivos do banco de dados
   - Tenta abrir os arquivos dim_user.parquet e fact_ride.parquet
   - Retorna `True` se ambos existirem, `False` caso contrário

2. `creat_database(path)`:
   - Cria nova estrutura de banco de dados
   - Cria tabela de dimensões do usuário (dim_user)
   - Cria tabela fato de caronas (fact_ride)
   - Salva ambas as tabelas em formato .parquet

3. `show_help()`:
   - Exibe o guia completo de ajuda do sistema
   - Fornece instruções detalhadas para cada funcionalidade

4. `show_quick_help()`:
   - Exibe versão resumida do menu de ajuda
   - Mostra descrição básica de cada opção

### 3.3 Funções Utilitárias (utils.py)
O arquivo utils.py contém funções auxiliares para geração de IDs e chaves.

#### Funções:
1. `gen_id(df)`:
   - Gera ID único para usuários/caronas
   - Parâmetros:
     - df: DataFrame contendo os IDs existentes
   - Funcionamento:
     - Gera número aleatório entre 1 e 9999999
     - Verifica se já existe no DataFrame
     - Repete até encontrar número único
   - Retorna: ID único gerado

2. `gen_privete_key(df)`:
   - Gera chave privada única para usuários
   - Parâmetros:
     - df: DataFrame contendo as chaves existentes
   - Funcionamento:
     - Similar ao gen_id
     - Garante unicidade da chave privada
   - Retorna: Chave privada única

## 4. Estrutura de Dados

### 4.1 Tabela Dimensão (dim_user)
```python
columns_user = [
    'id',          # ID único do usuário
    'name',        # Nome completo
    'email',       # Email para contato
    'phone',       # Telefone
    'private_key'  # Chave privada para autenticação
]
```

### 4.2 Tabela Fatos (fact_ride)
```python
columns_ride = [
    'id',                 # ID único da carona
    'user_id',           # ID do usuário ofertante
    'local_origin',      # Local de partida
    'local_destination', # Local de destino
    'datatime'          # Data e hora da carona
]
```
## 5. Fluxo de Funcionamento

1. Verificação inicial:
   - Checa existência do banco de dados
   - Cria estrutura se necessário

2. Loop principal:
   - Exibe menu de opções
   - Processa escolha do usuário
   - Executa funcionalidade correspondente
   - Salva alterações nos arquivos .parquet

## 6. Tratamento de Dados
- Padronização de 'UNB' sempre em maiúsculo
- Conversão de strings de data/hora para formato datetime
- Validação de chave privada para ofertas de carona

## 7. Como Executar o Projeto

### 7.1 Pré-requisitos
```bash
pip install pandas pyarrow
```

### 7.2 Execução
```bash
python main.py
```


## 8. Detalhes de Implementação

### 8.1 Gerenciamento de Dados
- Utilização de arquivos .parquet para persistência
- Verificação automática da existência do banco
- Criação automática das estruturas necessárias
- Garantia de unicidade de IDs e chaves privadas

### 8.2 Segurança
- Sistema de chaves privadas para autenticação
- Validação de dados em cada operação
- Separação de dados sensíveis em tabelas diferentes

### 8.3 Padronização
- Conversão automática de locais para maiúsculo
- Formatação consistente de data e hora
- Validação de entrada de dados

---
Desenvolvido para a disciplina de APC - UnB


