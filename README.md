# Sistema de Caronas UnB

Este projeto é uma aplicação Python para facilitar o compartilhamento de caronas entre membros da comunidade universitária da Universidade de Brasília (UnB). O sistema permite que usuários cadastrem ofertas de caronas e busquem caronas disponíveis de acordo com suas necessidades.

## Descrição

O **Sistema de Caronas UnB** oferece uma plataforma simples para conectar motoristas e passageiros da UnB, proporcionando a oferta e busca de caronas de forma eficiente e segura.

### Funcionalidades

1. **Cadastro de Usuário**: Permite o cadastro de usuários com dados como nome, email, telefone e região administrativa. O sistema gera automaticamente um ID único e uma chave privada para autenticação.

2. **Cadastro de Oferta de Carona**: Os usuários podem oferecer caronas, autenticando-se com a chave privada e informando detalhes como origem, destino e horário da carona.

3. **Busca de Carona**: Permite a busca por caronas de acordo com o local de origem, destino e intervalo de horário.

4. **Busca de Informações de Contato**: Permite buscar os dados de contato do usuário que ofereceu a carona, fornecendo nome e telefone.

## Estrutura do Projeto

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

### Bibliotecas Utilizadas

- **pandas**: Manipulação e análise de dados
- **pyarrow**: Suporte para arquivos `.parquet`



