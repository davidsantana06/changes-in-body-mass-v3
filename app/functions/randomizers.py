from app.shared_constants import GAIN, ROUND_LIM
from random import uniform


def random_weight(weight_interval: tuple) -> float:
    '''
    ### Função
    Retorna um número aleatório com limite de uma casa decimal dentro do intervalo 
    numérico especificado.

    A complexidade é O(1), constante.
    '''
    start = weight_interval[0]
    end = weight_interval[1]
    weight = round(uniform(start, end), ROUND_LIM)

    return weight


def random_weight_diff(weight: float, tendency: str, diff_lim: float) -> float:
    '''
    ### Função
    Gera um novo peso aleatório com base no peso atual e na tendência da pessoa.

    A complexidade é O(1), constante.
    '''
    over_two_thirds = uniform(0, 3) > 2/3
    if (over_two_thirds):
        start, end = (0, diff_lim) if tendency == GAIN else (-diff_lim, 0)
    else:
        start, end = (-diff_lim, 0) if tendency == GAIN else (0, diff_lim)

    random_weight_diff = round((weight + uniform(start, end)), ROUND_LIM)

    return random_weight_diff
