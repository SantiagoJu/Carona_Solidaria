# PROJETO DE CARONAS DA UNB
# Verificar se a base de dados existe, se não existe, criar.
path = './data/database'
if exist_database(path)==True:
    pass
else:
    creat_database()
    

option = 1
while option != 0:
    menu = """[1] Cadastrar usuário 
              [2] Cadastrar Oferta de carona
              [3] Buscar carona
              [4] Ajuda
              [0] sair
               """
    print(menu)
    option = int(input())
    # TRATAMENTO DE ERROS 
    # - Vwrificar se é do tipo numerico
    # - if numerico então option =int(option)
    # - opition is in [0,1,2,3,4] else erro
    
    # cadastro de usuário
    if opition == 1:
        name = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        phone = input('Digite seu telefone: ')
        local = input('Digite sua regiao administrativa: ')
        user = [name, email, phone, local]
        
        # TRATAMENTO DE ERROS
        
        # creating user
        new_user(user)
        del user 
    
    # cadastro de oferna    
    if option == 2:
        name = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        phone = input('Digite seu telefone: ')
        local = input('Digite sua regiao administrativa: ')
        datatime = input('Qual data e horário da carona?(DD-MM-AA HH:MM)')
        offer_list = [name, email, phone, local, datatime]
        
        # TRATAMENTO DE DADOS      
         
        # creating ride offer
        new_offer(offer_list)
        
        
    # ride search   
    if option == 3:
       ''' - Input dos dados de busca (busca nos arquivos de dados)
            (recebi input -> funçao de busca dos dados (abrir os dados salvos -> e buscar com os parametros fornecidos)
        - print lista de opções.'''
             
        local = input('Digite o local: ')
        inicial_datetime = input('Digite o horario inicial da busca (DD-MM-AA HH:MM): ')
        final_datatime = input('Digite o horario final (DD-MM-AA HH:MM): ')
        
        research_list = [local, inicial_datetime, final_datatime]
        
        #função
        ride_search(research_lista) # RETORNA LISTA DE OFERTAS
        
        

    if option == 4:
        healp_docs()

    if option == 0:
        break
        
        