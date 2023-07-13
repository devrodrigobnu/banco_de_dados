import os
import sqlite3
import pandas as pd

# Instalar o pandas na nossa maquina local
# com o comando pip install pandas

def executar_comandos_sql(sql_string):
    """ Primeira docstring: Função para executar comandos SQL na base de dados usando pandas"""

    # Criar a conexão com o banco de dados
    conexao = sqlite3.connect('mydatabase.db')

    # A função do pandas chamadas 'read_sql_query', esse comanda ele executa SQL
    # e espera como parâmetros uma string com o SQL a ser executado
    # e ele também espera a conexão com a base de dados
    retorno_do_sql = pd.read_sql_query(sql_string, conexao)

    # Fechar a conexão
    conexao.close()

    # Retornar os dados do query (ou seja, da busca SQL)
    return retorno_do_sql

def mostrar_opcoes(colunas_lista):
    """Função para mostrar as opções disponíveis do programa para o usuário """

    # Printar os dados usando um for na lista com as colunas disponíveis
    print('Colunas disponíveis:')
    for indice, coluna_string in enumerate(colunas_lista):
        print(f'Coluna {indice + 1}: {coluna_string}')
    # Enumerate permite que seja possível rodar o for com duas variáveis
    # uma sendo o índice (i) da linha, e a outra sendo o valor (dado/informacao)

    print()

def retornar_media_coluna(coluna_nome):
    """Função para retornar média de uma coluna informada pelo usuário """

    # Comando SQL
    sql_string = f'select avg({coluna_nome}) from usuarios'
    
    # Executar SQL
    retorno = executar_comandos_sql(sql_string)
   
    # Mostrar o resultado
    print('\n')
    print('MÉDIA:')
    print(retorno)


def contar_linhas_coluna(coluna_nome):
    """Função para dar um COUNT na coluna informada pelo usuário """
    
    # Comando SQL
    sql_string = f'select count({coluna_nome}) from usuarios'
    # Executar SQL
    retorno = executar_comandos_sql(sql_string)

    # Mostrar o resultado
    print('\n')
    print('COUNT:')
    print(retorno)

def buscar_palavras_em_colunas(nome_coluna, tipo_busca, string_usuario):
    """ Função para buscar partes específicas das palavras usando LIKE """

    # Criar a string com o padrão da palavra que será buscada
    string_de_busca = ''
    if tipo_busca == 'start':
        string_de_busca = f"'{string_usuario}%'"
    elif tipo_busca == 'end':
        string_de_busca = f"'%{string_usuario}'"    
    elif tipo_busca == 'middle':
        string_de_busca = f"'%{string_usuario}%'"
    else:
        print('Tipo de busca é inválido')

    # Comando SQL
    sql_string = f"""
        
        select * from usuarios\
        where {nome_coluna} LIKE {string_de_busca}

    """

    # Executar SQL
    retorno = executar_comandos_sql(sql_string)

    # Mostrar o resultado
    print('\n')
    print('LIKE:')
    print(retorno)
    
def retornar_min_e_max_coluna(coluna_nome):
    """ Função para mostrar o maior e o menor valor de uma coluna"""

    # Comando SQL
    sql_string = f'select MAX({coluna_nome}), MIN({coluna_nome}) from usuarios'

    # Executar SQL
    retorno = executar_comandos_sql(sql_string)

    # Mostrar o resultado
    print('\n')
    print('MIN-MAX:')
    print(retorno)

# START
os.system('cls')

# Usando o PRAGMA table_info() para buscar informações sobre a tabela usuário
sql_retorno_colunas = 'PRAGMA table_info(usuarios)' 
# Executando o SQL
colunas = executar_comandos_sql(sql_retorno_colunas)
# Separando apenas as colunas do retorno SQL
colunas_lista = colunas['name'].tolist()
# Variável contador que vai contar quantas operações no banco de dados foram realizadas.
contador = 0

print(colunas_lista)

rodar_programa = True
while rodar_programa is True:
    print('\n')
    mostrar_opcoes(colunas_lista)
    print('Digite s para sair\n')

    # Por padrão, o input recebe strings
    coluna_posicao = input('Informe a posição da coluna a manipular: ')

    if coluna_posicao == 's':
        break
    
    # Converter o valor informado para inteiro
    coluna_posicao = int(coluna_posicao)

    # Validar a posicao informada
    if coluna_posicao > 0 and coluna_posicao <= len(colunas_lista):
        # Criar a variavel para o nome da coluna    
        # Extrair o nome da coluna da lista de colunas usando a posicao informada
        coluna_nome = colunas_lista[coluna_posicao - 1]
        print(f'\nColuna {coluna_nome} selecionada com sucesso!')  
          
        # Mensagem string do menu operações  
        menu_operacoes = '\n1 - Média'
        menu_operacoes += '\n2 - Count'
        menu_operacoes += '\n3 - Busca usando LIKE'
        menu_operacoes += '\n4 - Min / Max'
        menu_operacoes += '\n5 - Informe a operação: '

        # Converter operação para inteiro
        operacao = int(input(menu_operacoes))

        if operacao == 1:
            # Chamar a função que retornar a média da coluna
            retornar_media_coluna(coluna_nome)

        elif operacao == 2:
            # Chamar a função que retorna a média da coluna
            contar_linhas_coluna(coluna_nome)

        elif operacao == 3:
            # Menu para o input
            menu_input = '\n - start'
            menu_input += '\n - middle'
            menu_input += '\n - end'
            menu_input += '\n - Informe a opção: '

            # Usar o int para transformar a buscam em um número
            tipo_busca = input(menu_input)

            # Ler a string que será usada para a busca no banco de dados
            string_usuario = input('\nInforme a string que irá para a busca no banco: ')

            # Chamar a função para buscar a "string_usuário" 
            # Passando os parâmetros informados
            buscar_palavras_em_colunas(coluna_nome, tipo_busca, string_usuario)
            
        elif operacao == 4:
            # Retonar o menor e o maior valor da coluna
            retornar_min_e_max_coluna(coluna_nome)
        else:
            print('\nFoi informado uma operação inválida!')
    else:
        print('Informe uma posição válida!')
    
    
    
    





















# retorno = executar_comandos_sql('select * from usuarios')
# print(retorno)
# mostrar_opcoes(['name', 'age', 'email'])
# retornar_media_coluna('idade')
# contar_linhas_coluna('idade')
# buscar_palavras_em_colunas('nome', 'start', 'a')
# retornar_min_e_max_coluna('idade')


