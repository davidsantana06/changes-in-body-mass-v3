from app.functions.randomizers import random_weight_diff
from app.shared_constants import ROUND_LIM
from threading import Thread
from time import sleep


DIFF_LIM = 0.2
HISTORY_LIM = 10
NORMAL_WEIGHT = 76.3
SLEEP_TIME = 1
VARIANCE = 1

class Person:
    '''
    ### Classe
    Representa os dados de uma pessoa, incluindo informações como seu histórico de 
    pesagens. As pesagens são atualizadas dinamicamente por meio de uma thread.
    '''

    def __init__(self, id: int, tendency: str, fst_weight: float):
        self.__id = id
        self.__tendency = tendency
        self.__weight_history = [fst_weight]

        self.__warning = ''
        self.__variance_pairs = []
        self.__pair_count = 0

        self.__thread_running = False
        self.__thread = Thread(target=self.__update_weight_history)


    # > MÉTODOS GET
    def get_id(self) -> int:
        return self.__id

    def get_tendency(self) -> str:
        return self.__tendency

    def get_current_weight(self) -> float:
        return self.__weight_history[-1]

    def get_weight_history(self) -> list[float]:
        return self.__weight_history

    def get_variance_pairs(self) -> list[str]:
        return self.__variance_pairs

    def get_warning(self) -> str:
        return self.__warning


    # > MÉTODOS SET
    def set_thread(self, thread: Thread):
        self.__thread = thread


    # MÉTODOS POP
    def pop_thread(self) -> Thread:
        thread = self.__thread
        self.__thread = None

        return thread


    # > MÉTODOS RELATIVOS AO FUNCIONAMENTO DA THREAD
    def toggle_thread(self):
        '''
        ### Método
        Alterna o estado de execução da thread entre ativo e inativo, dependendo do seu
        estado atual.

        A complexidade é O(1), constante.
        '''
        if not self.__thread_running and self.get_current_weight() > NORMAL_WEIGHT:
            self.__thread_running = True
            self.__thread.start()
        else:
            self.__thread_running = False


    def __calculate_weight_diff(self, weight: float, new_weight: float) -> tuple:
        '''
        ### Método
        Calcula e retorna a diferença entre a última pesagem e a pesagem atual.

        A complexidade é O(1), constante.
        '''
        day = len(self.__weight_history)
        weight_diff = round(new_weight - weight, ROUND_LIM)

        return (day, weight_diff)

    def __update_variance_pairs(self):
        '''
        ### Método
        Percore o histórico de pesagens a partir do último índice, verificando se as 
        variações são iguais ao limite definido. Caso sejam, as variações são anexadas 
        à lista de variâncias.

        A complexidade desta função é O(n), ou seja, linear, uma vez que o número de 
        passos realizados aumenta em conformidade com o histórico de pesagens.
        '''
        len_wh = len(self.__weight_history)
        idx_cw = len_wh - 1
        limit = len_wh - 2

        for i, weight in enumerate(self.__weight_history[:limit]):
            pair_variance = round(abs(self.get_current_weight() - weight), ROUND_LIM)

            if pair_variance == VARIANCE:
                self.__pair_count += 1

                if self.__pair_count % 11 == 0:
                    self.__variance_pairs.append(f"\n{' ' * 9}({idx_cw} e {i})")
                else:
                    self.__variance_pairs.append(f'({idx_cw} e {i})')

    def __update_weight_history(self):
        '''
        ### Método
        Atualiza o histórico de pesagens com um novo peso gerado aleatoriamente. Se o 
        peso gerado atingir o limite mínimo estipulado, a thread finaliza a sua 
        execução.

        A complexidade é O(1), constante.
        '''
        while self.__thread_running:
            sleep(SLEEP_TIME)

            current_weight = self.get_current_weight()

            new_weight = random_weight_diff(current_weight, self.__tendency, DIFF_LIM)

            self.__weight_history.append(new_weight)
            day, weight_diff = self.__calculate_weight_diff(current_weight, new_weight)

            if weight_diff > 0:
                warning_msg = f'\n> Dia {day} ganhou {weight_diff} Kg'

                if not self.__warning:
                    warning_msg = f'ID {self.__id}' + warning_msg

                self.__warning += warning_msg

            self.__update_variance_pairs()

            if new_weight <= NORMAL_WEIGHT:
                self.toggle_thread()


    # MÉTODOS SOBRESCRITOS
    def __str__(self):
        return '' \
            + f'ID {self.__id}\n' \
            + f'> Tendência: {self.__tendency}\n' \
            + f'> Pesagens: {self.__weight_history[-HISTORY_LIM:]}'
