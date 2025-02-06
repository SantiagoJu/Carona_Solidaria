import pandas as pd

class DataBase:
    def exist_database(path):
        return False

    def creat_database(path):
        '''
        Criando uma nova tabela na base de dados e salvando no tipo de arquivo .parquet.
        '''

        # Criando uma nova tabela de dimensões do usuário
        colums_user = ['name', 'email', 'phone']
        df_users = pd.DataFrame(columns=colums_user)

        # Criando a tabela fato de caronas
        columns_ride = ['local', 'datatime']
        df_ride = pd.DataFrame(columns=columns_ride)

        # Salvando os arquivos de banco de dados em .parquet
        # Dimensões do usuário
        save_path_user = path + 'dim_user.parquet'
        df_users.to_parquet(save_path_user)

        # Fact Ride(?)
        save_path_ride = path + 'fact_ride.parquet'
        df_ride.to_parquet(save_path_ride)

    def new_user():
        pass

    def new_offer():
        pass

    def ride_search():
        pass