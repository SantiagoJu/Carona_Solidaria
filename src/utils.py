import random

###CRIAR FUNÇÃO PARA GERAR ID:
#Gerar um número int de id randomico;
#Verificar se o número gerado já existe na coluna id no banco de dados;
#Se sim, gerar outro
#Se não, retornar o número gerado.

def gen_id(df):
    condition = True
    while condition:
        num = random.randint(1, 9999999)
        # Se o número aleatório existir no banco de dados gerado, condition == True
        # Se o número aleatório NÃO existir no banco de dados gerado, condition == False  
        condition = df.isin([num]).any()
        # any(função que diz se existem "algum True" da condição citada anteriormente).Serve para retornar se exite algum True na lista que o isin(função de comparação) criou. 
        if condition == True:
            continue
        # Se o número aleatório gerado NÃO existir no banco de dados retorna NUM
        if condition == False:
            break
    return num

def gen_privete_key(df):
    condition = True
    while condition:
        num = random.randint(1, 9999999)
        # Se o número aleatório existir no banco de dados gerado, condition == True
        # Se o número aleatório NÃO existir no banco de dados gerado, condition == False  
        condition = df.isin([num]).any()
        # any(função que diz se existem "algum True" da condição citada anteriormente).Serve para retornar se exite algum True na lista que o isin(função de comparação) criou. 
        if condition == True:
            continue
        # Se o número aleatório gerado NÃO existir no banco de dados retorna NUM
        if condition == False:
            break
    return num


    