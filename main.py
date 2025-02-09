# PROJETO DE CARONAS DA UNB
from src.database import DataBase as db
from src.utils import *


import pandas as pd


#Verificar se a base de dados existe, se não existe, criar.
path = '.\\data\\'
if db.exist_database(path)==True:
    pass
else:
    db.creat_database(path)
 
 
# Abrindo o banco de dados como DataFrame.
# Caminho do banco de dados dim_user.
path_dim_user = '.\\data\\' + 'dim_user.parquet'
# a biblioteca pandas lê o banco de dados com a função read_parquet.
dim_user = pd.read_parquet(path_dim_user)

# Caminho do banco de dados fact_ride.
path_fact_ride = '.\\data\\' + 'fact_ride.parquet'
# a biblioteca pandas lê o banco de dados com a função read_parquet.
fact_ride = pd.read_parquet(path_fact_ride)

print(dim_user)
print(40*'=')
print(fact_ride)

option = 1
while option != 0:
    
    menu = """=================== MENU ===================== 
              [1] Cadastrar usuário 
              [2] Cadastrar Oferta de carona
              [3] Buscar carona 
              [4] Buscar informações de contato da carona
              [5] Ajuda
              [0] sair
               """
    print(menu)
    option = int(input())
    # TRATAMENTO DE ERROS 
    # - Verificar se é do tipo numerico
    # - if numerico então option =int(option)
    # - opition is in [0,1,2,3,4] else erro
    
    # cadastro de usuário
    if option == 1:
        name = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        phone = int(input('Digite seu telefone usando digitos de 0 a 9: '))
        local = input('Digite sua regiao administrativa: ')
        idd = gen_id(dim_user['id'])
        private_key = gen_privete_key(dim_user['private_key'])
        user = {'id'   : idd,
                'name' : name,
                'email': email,
                'phone': phone,
                'local': local,
                'private_key' : private_key}
        
        user_append = pd.Series(user)
    
        # TRATAMENTO DE ERROS
        
        # creating user
        # Adicionando o novo usuário ao Dataframe.
        dim_user = pd.concat([dim_user, user_append.to_frame().T], ignore_index=True)
        #dim_user = pd.concat([dim_user, user], axis=0, ignore_index=True)
        print("ARMAZENE SUA CHAVE PRIVADA!!") #arrumar mensagem
        print("Sua chave privada é: ", private_key)
        del user 

    # cadastro de oferna    
    if option == 2:
        # Verificar o usuário
        authetication = int(input('Digite a sua chave privada: ')) # VALIDAR ENTRADA
        # Verificando se existe a chave authentication na coluna private_key da tabela dim_user(dataframe)
        # any() retorna se existe algum valor ao invés de retprnar uma lista de valores.
        valid_auth = dim_user['private_key'].isin([authetication]).any()
        
        # Se a validação de autenticação não der certo, eke retorna para o menu. 
        if valid_auth == False:
            continue 
        
        local_origin = input('Digite sua regiao administrativa: ')
        
        if local_origin.upper() != 'UNB':
            local_destination = 'UNB'
            
        if local_origin.upper() == 'UNB':
            local_destination = input('Digite seu local de destino: ')
        
        # Padronizando 'UNB' para ficar sempre em maísculo.
        #if local_origin.upper() == 'UNB':
          #  local_origin = local_origin.upper()
        
        #if local_destination.upper() == 'UNB':
        #    local_destination = local_destination.upper()
        local_destination = local_destination.upper()
        local_origin = local_origin.upper()
        
        
        datatime = input('Qual data e horário da carona?(DD-MM-AA HH:MM)') # Tipo string
        # Transformando a string datatime no tipo de dado "datatime"
        datatime = pd.to_datetime(datatime, format="%d-%m-%y %H:%M") # Tipo datatime
        
        #  Gerando uma id primário(a chave principal da carona) para tabela fatos.
        idd = gen_id(fact_ride['id'])
        
        # Filtrando o usuário pela chave privada
        # Criando filtro
        filtro = dim_user["private_key"] == authetication
        # Aplicando filtro criado anteriormente: Retorna apenas as linhas que contêm a chave privada
        user_id = dim_user[filtro]["id"].iloc[0]
        
        # Criando dicionário que será transformado em DataFrame.
        offer_list = {'id' : idd,
                      'user_id': user_id,
                      'local_origin' : local_origin,
                      'local_destination': local_destination,
                      'datatime': datatime}
                      
        
        # Adicionando dados no banco de dados.
        # Transformando a offer_list em uma DataFrame do tipos Series.
        offer_list_append = pd.Series(offer_list)
        # Adicionando (concatenando) a lista (offer_list) ao banco de dados fatos.
        fact_ride = pd.concat([fact_ride, offer_list_append.to_frame().T], ignore_index=True)

        
        # TRATAMENTO DE DADOS      
         
         
    # ride search   
    if option == 3:
        # RECEBENDO DADOS 
        # Input dos dados de busca (busca nos arquivos de dados)
       
        local_origin = input('Digite o seu local de origem: ')
        
        if local_origin.upper() != 'UNB':
            local_destination = 'UNB'
            
        if local_origin.upper() == 'UNB':
            local_destination = input('Digite seu local de destino: ')
        
        # Padronizando para ficar sempre em maísculo.
        local_origin = local_origin.upper()
        local_destination = local_destination.upper()
        
        # Transformando o inicial_datetime do tipo string para o tipo datatime.
        inicial_datatime = input('Digite o horario inicial da busca (DD-MM-AA HH:MM): ') # Tipo string
        inicial_datatime = pd.to_datetime(inicial_datatime, format="%d-%m-%y %H:%M") # Tipo datatime
        
        # Transformando o final_datetime do tipo string para o tipo datatime.
        final_datatime = input('Digite o horario final (DD-MM-AA HH:MM): ') # Tipo string
        final_datatime = pd.to_datetime(final_datatime, format="%d-%m-%y %H:%M") # Tipo datatime
        
        # BUSCANDO DADOS
        
        # criando filtro de dados
        # Vai buscar na tabela fatos todos os locais que forem iguais ao input
        filter_local_origin = fact_ride["local_origin"].str.contains(local_origin) 
        filter_local_destination = fact_ride["local_destination"].str.contains(local_destination)
        # Filtrando data e hora
        filter_delta_time = (fact_ride["datatime"] >= inicial_datatime) & (fact_ride["datatime"] <= final_datatime)
        # Faz com que todos os filtros ocorram ao mesmo tempo.
        filtro = filter_local_origin & filter_local_destination & filter_delta_time
    
        # Printando dados filtrados
        print(fact_ride[filtro])
        
     
    if option == 4:
        user_id = int(input('Digite o id de usuário: '))
        columns = ['name', 'phone']
        filtro = dim_user['id'] == user_id
        print(dim_user[filtro][columns])
        
    if option == 5:
        db.show_help()  

    if option == 0:
        break
        
#Salvando o banco de dados tabela de dimensão usuário
dim_user.to_parquet(path_dim_user)

#Salvando o banco de dados tabela fatos carona
fact_ride.to_parquet(path_fact_ride)



