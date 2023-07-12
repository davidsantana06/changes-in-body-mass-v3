from app import mini_world, PERSON_LIM
from app.functions.chart import show_chart
from app.functions.excel import convert_to_df, write_excel
from app.functions.mini_world import (
    data_decrypt, data_extraction, enumerate_weight_history, sort_by_id, 
    sort_by_weight, toggle_threads, variance_pairs, warning_report
)
from app.functions.utils import format_text as fmt, terminal_text as txt, validate_id
from re import match


def handle_operation(op: str) -> tuple[str, bool]:
    '''
    ### Função
    Possibilita a interação do usuário com a aplicação, com base na operação
    fornecida como parâmetro.
    '''
    result = ''
    should_continue = True

    if match(r'^[0-8]$', op):
        if op == '0':
            print('\n' + txt('kill_threads'))
            toggle_threads(mini_world)
            should_continue = False
            result = txt('good_bye')
        else:
            # Antes de realizar qualquer operação, é necessário descriptografar 
            # os dados presentes no mini mundo
            decrypted_mw = data_decrypt(mini_world)

            match (op):
                case '1':
                    data = data_extraction(decrypted_mw)
                    result = fmt(data)
                case '2':
                    valid_id = False

                    while not valid_id:
                        id = input('_Informe o ID: ')
                        valid_id = validate_id(id, PERSON_LIM)

                        if valid_id:
                            enumerated_history = enumerate_weight_history(decrypted_mw, int(id))
                            result = fmt(enumerated_history)
                        else:
                            print('\n' + txt('inv_inp'))
                case '3':
                    var_pairs = variance_pairs(decrypted_mw)
                    result = fmt(var_pairs)
                case '4':
                    warning = warning_report(decrypted_mw)

                    if warning:
                        result = fmt(warning)
                    else:
                        result = txt('no_report')
                case '5':
                    show_chart(decrypted_mw)
                    result = txt('returning')
                case '6':
                    sort_by_weight(decrypted_mw, mini_world)
                    result = txt('sort')
                case '7':
                    sort_by_id(decrypted_mw, mini_world)
                    result = txt('sort')
                case '8':
                    dataframe = convert_to_df(decrypted_mw)
                    write_excel(dataframe)
                    result = txt('write_excel')
    else:
        result = txt('inv_inp')

    return (result, should_continue)


if __name__ == '__main__':
    print(txt('welcome'))
    should_continue = True

    while should_continue:
        print(f"\n{txt('main_menu')}")
        op = input('_Informe a operação: ')

        result, should_continue = handle_operation(op)
        print(f'\n{result}')
