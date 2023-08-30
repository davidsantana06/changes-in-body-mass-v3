from app.classes.person import Person
from app.shared_constants import SRC_FOLDER
from pandas import DataFrame
from typing import List


FILE_PATH = f'{SRC_FOLDER}/mini_world.xlsx'

def convert_to_df(decrypted_mw: List[Person]) -> DataFrame:
    '''
    ### Função (Extra)
    Converte a relação de dados do mini mundo em um objeto DataFrame.
    '''
    max_len = max(len(person.get_weight_history()) for person in decrypted_mw)
    days = [f'{(i + 1)}' for i in range(max_len)]
    person_dict = {'Dia': days}

    for person in decrypted_mw:
        id = person.get_id()
        weight_history = person.get_weight_history()
        list_len = len(weight_history)

        formatted_history = []
        for weight in weight_history:
            formatted_weight = f"{str(weight).replace(',', '.')} Kg"
            formatted_history.append(formatted_weight)

        diff_len = max_len - list_len
        comp_list = ['-'] * diff_len
        unified_lists = formatted_history + comp_list

        person_dict.update({f'ID {id}': unified_lists})

    dataframe = DataFrame(person_dict)

    return dataframe


def write_excel(dataframe: DataFrame):
    '''
    ### Função (Extra)
    Salva um objeto DataFrame como arquivo Excel no diretório raiz da aplicação.
    '''
    dataframe.to_excel(FILE_PATH, index=False)
