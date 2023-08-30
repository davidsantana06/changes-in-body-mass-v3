from app.classes.person import Person
from app.functions.criptography import encrypt
from pickle import dumps
from random import choice, randint


ALL_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
NUMBER_GAP = 26 - 9

class Container:
    '''
    ### Classe
    Representa o processo de encapsulamento e criptografia dos dados de uma pessoa. 
    O encapsulamento envolve a organização dos dados em uma estrutura coesa, 
    protegendo-os contra acesso não autorizado.
    '''

    def __init__(self, person: Person, waveforms: list):
        self.__person = person
        self.__waveforms = waveforms

    def encrypt_person(self) -> tuple[bytes, bytes]:
        '''
        ### Método
        Criptografa as informações da pessoa e retorna os dados criptografados, 
        juntamente com a chave necessária para realizar a descriptografia.

        A complexidade é O(1), constante.
        '''
        thread = self.__person.pop_thread()
        person, key = encrypt(dumps(self.__person), self.__random_value())
        self.__person.set_thread(thread)
        
        return (person, key)

    def toggle_thread(self):
        '''
        ### Método
        Realiza o intermédio entre o nível de encapsulamento e os dados da pessoa, 
        acessando o método correspondente à atividade da thread da pessoa.

        A complexidade é O(1), constante.
        '''
        self.__person.toggle_thread()

    def __random_value(self) -> str:
        '''
        ### Método
        Gera um valor aleatório com base na playlist da pessoa, representada por uma 
        lista contendo as ondas sonoras.

        A complexidade é O(1), constante.
        '''
        value = ''
        idx = randint(0, len(self.__waveforms) - 1)
        waveform = self.__waveforms[idx]

        for char in str(waveform):
            if char.isdigit():
                value += chr(int(char) + randint(0, NUMBER_GAP) + choice([ord('a'), ord('A')]))
            else:
                value += choice(ALL_CHARS)

        return value
