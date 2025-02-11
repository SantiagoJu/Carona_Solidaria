import pandas as pd

class DataBase:
    def exist_database(path):
        # Tentando abrir o banco de dados dimensão USER
        try:
            # Caminho para o banco de dados dimensão
            path_dim = '.\\data\\' + 'dim_user.parquet'
            # Abrindo o arquivo parquet com o Pandas
            # A biblioteca pandas tem uma função que lê arquvios parquet e
            # transforma em Dataframe.
            dim_user = pd.read_parquet(path_dim)
        # Se a abertura do arquivo falhar, retorna falso;
        # ADICIONAR PRINT
        except:
            return False
        # ADICIONAR PRINT
        
        # Tentando abrir o banco de dados FATOS.
        try:
            # Caminho para o banco de dados fact ride.
            path_dim = '.\\data\\' + 'fact_ride.parquet'
            # Abrindo o arquivo parquet com o Pandas
            fact_ride = pd.read_parquet(path_dim)
        # ADICIONAR PRINT
        except:
            return False
        #ADICIONAR PRINT
        
        return True
        
        
    def creat_database(path):
        """
        Criando uma nova tabela na base de dados e salvando no arquivo .parquet.
        Entrada: PATH::string para salvar o arquivo de banco de dados.
        Saída: arquivo .parquet.
        """

        # Criando uma nova tabela de dimensões do usuário
        colums_user = ['id',
                       'name',
                       'email',
                       'phone',
                       'private_key']
        
        df_users = pd.DataFrame(columns=colums_user)

        # Criando a tabela fato de caronas
        columns_ride = ['id',
                        'user_id',
                        'local_origin',
                        'local_destination',
                        'datatime']
        
        df_ride = pd.DataFrame(columns=columns_ride)

        # Salvando os arquivos de banco de dados em .parquet
        # Dimensões do usuário
        save_path_user = path + 'dim_user.parquet'
        df_users.to_parquet(save_path_user)

        # Tabela fato: Carona
        save_path_ride = path + 'fact_ride.parquet'
        df_ride.to_parquet(save_path_ride)

    def ride_search():
        pass
    
    def show_help():
        help_text = """
        =================================================================
                            SISTEMA DE CARONAS UNB
                                GUIA DE AJUDA
        =================================================================

        1. CADASTRO DE USUÁRIO
           - Preencha os campos com as informações pedidas
           - Ao se cadastrar, você receberá uma chave privada
           - Esta chave será necessária para cadastrar ofertas de carona
           - Guarde sua chave em segurança

        2. CADASTRAR OFERTA DE CARONA
           - Digite sua chave privada para autenticação
           - Informe:
             * Local de origem
             * Local de destino
             * Data e horário
           - Sua oferta ficará disponível para outros usuários
           - Importante lembrar que as informações ficaram salvas depois que sair do programa na opção 0.

        3. BUSCAR CARONA
           - Digite:
             * Local de origem desejado
             * Local de destino desejado
             * Data/horário pretendido
           - O sistema mostrará caronas disponíveis
           - Para cada carona, será exibido um ID do motorista
           - Pesquise o trecho de tempo em que sua carona se encontra.
           - Exemplo de pesuisa de caronas às 19:00 do dia 10/10/25:
           - Digite o horario inicial da busca (DD-MM-AA HH:MM): 10-10-25 18:00
           - Digite o horario final (DD-MM-AA HH:MM): 10-10-25 20:00

        4. BUSCAR INFORMAÇÕES DE CONTATO
           - Digite o ID do motorista obtido na busca
           - Você receberá:
             * Informações de contato do motorista
             * Detalhes específicos do ponto de encontro
             * Horário exato da carona

        5. DICAS DE SEGURANÇA
           - Sempre verifique as informações do motorista
           - Combine o ponto de encontro em local público
           - Compartilhe os detalhes da carona com alguém de confiança
           - Em caso de dúvidas, utilize os canais oficiais da UNB

        0. SAIR
           - Encerra o programa e salva as informações digitadas

        Para mais informações ou suporte, entre em contato com a administração
        do sistema através dos canais oficiais da UNB.
        =================================================================
        """
        print(help_text)
        input("\nPressione ENTER para voltar ao menu principal...")

        def show_quick_help():
            """
            Displays a shorter version of help with just the basic menu options.
            """
            quick_help = """
        [1] Cadastrar usuário - Criar nova conta e receber chave privada
        [2] Cadastrar Oferta - Oferecer uma carona
        [3] Buscar carona - Procurar caronas disponíveis
        [4] Buscar informações - Ver dados de contato do motorista
        [5] Ajuda - Mostrar este guia
        [0] Sair - Encerrar o programa
        """
            print(quick_help)
