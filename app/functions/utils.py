def comp_warning_msg(id: int, day: int, weight_diff: float):
    '''
    ### Função (Extra)
    Compõe uma mensagem de aviso conforme o padrão de exibição.
    '''
    warning_msg = f'ID {id}\n> Dia {day} ganhou {weight_diff} Kg'

    return warning_msg


def format_text(msg: str) -> str:
    '''
    ### Função (Extra)
    Formata uma mensagem de texto (string) para o padrão de exibição.
    '''
    msg_list = msg.splitlines()
    larger_line = max(len(line) for line in msg_list)
    formatted_lines = [f'| {line:<{larger_line}} |\n' for line in msg_list]
    formatted_msg = ''.join(formatted_lines)
    hyphens = '-' * (larger_line + len('||'))

    return (f'|{hyphens}|\n{formatted_msg}|{hyphens}|')


def terminal_text(name: str) -> str:
    '''
    ### Função (Extra)
    Retorna um texto com base no nome informado como parâmetro.
    '''
    txt = ''

    match (name):
        case 'welcome':
            txt = '+-+-+-+-+-+-+-+-+-+-+-+-\n' \
                + '- Changes in Body Mass +\n' \
                + '+     by David Santana -\n' \
                + '-+-+-+-+-+-+-+-+-+-+-+-+'
        case 'main_menu':
            txt = '                >> MENU PRINCIPAL <<                \n' \
                + '----------------------------------------------------\n' \
                + '> [1] Exibir as últimas 10 pesagens de cada pessoa  \n' \
                + '> [2] Exibir todos os dados de uma só pessoa        \n' \
                + '> [3] Exibir os pares de semanas com variação de 1Kg\n' \
                + '> [4] Exibir o monitoramento do mini mundo          \n' \
                + '> [5] Exibir o gráfico sobre a relação de peso atual\n' \
                + '> [6] Ordenar o mini mundo por peso atual           \n' \
                + '> [7] Ordenar o mini mundo por ID                   \n' \
                + '> [8] Salvar o mini mundo como tabela Excel         \n' \
                + '> [0] Encerrar aplicação                            '
        case 'sort':
            txt = '             > ! <             \n' \
                + '-------------------------------\n' \
                + 'MINI MUNDO ORDENADO C/ SUCESSO!'
        case 'inv_inp':
            txt = '        > ! <        \n' \
                + '---------------------\n' \
                + 'A ENTRADA É INVÁLIDA!\n'
        case 'no_report':
            txt = '              > ! <            \n' \
                + '-------------------------------\n' \
                + 'NÃO FORAM IDENTIFICADOS AVISOS!'
        case 'returning':
            txt = '        > ! <        \n' \
                + '---------------------\n' \
                + 'VOLTANDO AO TERMINAL!'
        case 'kill_threads':
            txt = '                 > ! <                 \n' \
                + '---------------------------------------\n' \
                + 'AS THREADS ESTÃO SENDO ENCERRADAS (...)'
        case 'write_excel':
            txt = '                 > ! <                 \n' \
                + '---------------------------------------\n' \
                + 'ARQUIVO SALVO NA PASTA RAIZ DO PROJETO!'
        case 'good_bye':
            txt = '+-+-+-+-+-+\n' \
                + '- See ya! -\n' \
                + '+-+-+-+-+-+'

    if (name not in ['welcome', 'good_bye']):
        txt = format_text(txt)

    return txt


def validate_id(id: str, person_lim: int) -> bool:
    '''
    ### Função (Extra)
    Verifica a validade do identificador fornecido como parâmetro.
    '''
    valid_id = False

    if (id.isdigit() and len(id) <= len(str(person_lim))):
        int_id = int(id)

        if (1 <= int_id <= person_lim):
            valid_id = True

    return valid_id
