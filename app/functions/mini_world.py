from app.classes.container import Container
from app.classes.person import Person
from app.functions.criptography import decrypt
from pickle import loads


# > FUNÇÕES GERAIS
def data_decrypt(mini_world: list[Container]) -> list[Person]:
    '''
    ### Função
    Descodifica os dados do mini-mundo e retorna uma lista com todas as pessoas, sem 
    nenhum tipo de encapsulamento adicional.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a quantidade de pessoas armazenadas no mini-mundo.
    '''
    decrypted_mw = []

    for container in mini_world:
        person, key = container.encrypt_person()
        decrypted_person = loads(decrypt(person, key))
        decrypted_mw.append(decrypted_person)

    return decrypted_mw


def data_extraction(decrypted_mw: list[Person]) -> str:
    '''
    ### Função
    Extrai os dados presentes no mini mundo e formata a exibição para uma melhor
    visualização.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a quantidade de pessoas armazenadas no mini-mundo.
    '''
    data_str = ''
    last_person = len(decrypted_mw) - 1

    for idx, person in enumerate(decrypted_mw):
        data_str += str(person)

        if idx < last_person:
            data_str += '\n\n'

    return data_str


def toggle_threads(mini_world: list[Container]):
    '''
    ### Função
    Indica a alteração da atividade de cada uma das threads ligadas às pessoas 
    presentes no mini mundo.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a quantidade de pessoas armazenadas no mini-mundo.
    '''
    for container in mini_world:
        container.toggle_thread()



# > FUNÇÕES DE ORDENAÇÃO
def sort_by_id(decrypted_mw: list[Person], mini_world: list[Container]):
    '''
    ### Função
    Ordena de forma crescente todas as pessoas inclusas no mini mundo, conforme o 
    valor do identificador.

    A complexidade é O(n^2), ou seja, quadrática, por conta do algoritmo Selection 
    Sort, que implica na necessidade de percorrer a lista uma vez por iteração, 
    selecionando o menor elemento e situando-o na posição correta.
    '''
    person_count = len(decrypted_mw)

    for i in range(person_count):
        min_index = i
        min_id = decrypted_mw[min_index].get_id()

        for j in range((i + 1), person_count):
            j_id = decrypted_mw[j].get_id()

            if j_id < min_id:
                min_index = j
                min_id = j_id

        decrypted_mw[i], decrypted_mw[min_index] = decrypted_mw[min_index], decrypted_mw[i]
        mini_world[i], mini_world[min_index] = mini_world[min_index], mini_world[i]


def sort_by_weight(decrypted_mw: list[Person], mini_world: list[Container]):
    '''
    ### Função
    Ordena de forma crescente todas as pessoas inclusas no mini mundo, conforme o 
    peso atual de cada uma.

    A complexidade é O(n^2), ou seja, quadrática, por conta do algoritmo Bubble Sort.
    Com ele, é necessário percorrer a lista inúmeras vezes, comparando e trocando a 
    posição dos elementos até que a lista esteja devidamente ordenada.
    '''
    person_count = len(decrypted_mw)

    for i in range(person_count - 1):
        swaped = False

        for j in range(person_count - i - 1):
            j_weight = decrypted_mw[j].get_current_weight()
            next_weight = decrypted_mw[j + 1].get_current_weight()

            if next_weight < j_weight:
                decrypted_mw[j], decrypted_mw[j + 1] = decrypted_mw[j + 1], decrypted_mw[j]
                mini_world[j], mini_world[j + 1] = mini_world[j + 1], mini_world[j]
                swaped = True

        if not swaped:
            break



# FUNÇÕES DE CONSULTA ESPECÍFICAS
def enumerate_weight_history(decrypted_mw: list[Person], id: int) -> str:
    '''
    ### Função
    Formata e enumera o histórico completo de pesagens de uma pessoa.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a extensão do histórico de pesagens da pessoa selecionada.
    '''
    weight_history = []

    for person in decrypted_mw:
        if person.get_id() == id:
            weight_history = person.get_weight_history()
            break

    enumerated_history = ''
    last_day = len(weight_history) - 1

    for day, weight in enumerate(weight_history):
        enumerated_history += f'Dia {day}\n> Peso: {weight} Kg'

        if day < last_day:
            enumerated_history += '\n\n'

    return enumerated_history


def variance_pairs(decrypted_mw: list[Person]) -> str:
    '''
    ### Função
    Percore todas as pessoas no mini mundo, resgatando as variações de par para cada
    uma delas.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a quantidade de pessoas armazenadas no mini-mundo.
    '''
    variance_pairs_data = []

    for person in decrypted_mw:
        id = person.get_id()
        pairs_with_variance = person.get_variance_pairs()

        if pairs_with_variance:
            pairs_str = ', '.join(pairs_with_variance)
            variance_pairs_data.append(f'ID {id}\n> Dias: [{pairs_str}]\n')
        else:
            variance_pairs_data.append(f'ID {id}\n> Dias: []\n')

    variance_pairs_data = '\n'.join(variance_pairs_data)

    return variance_pairs_data


def warning_report(decrypted_mw: list[Person]) -> str:
    '''
    ### Função
    Percorre todas as pessoas no mini mundo, a fim de resgatar os avisos referentes à 
    cada uma, caso tenha ocorrido ganho de peso.

    A complexidade é O(n), ou seja, linear, pois o número de passos aumenta de acordo 
    com a quantidade de pessoas armazenadas no mini-mundo.
    '''
    warning_report = ''

    for person in decrypted_mw:
        warning  = person.get_warning()

        if warning :
            warning_report += f'{warning}\n\n'

    warning_report = warning_report.rstrip()

    return warning_report
