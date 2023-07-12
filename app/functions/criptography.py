from cryptography.fernet import Fernet
from typing import Tuple


def encrypt(person_dumps: bytes, random_value: str) -> Tuple[bytes, bytes]:
    '''
    ### Função
    Criptografa um conjunto de dados e gera uma chave com base no valor aleatório 
    fornecido como parâmetro.

    A complexidade está intrinsecamente ligada a uma biblioteca externa, cujos detalhes
    não são necessários.
    '''

    # Gerar uma chave
    key = Fernet.generate_key() + random_value.encode()

    # Criar uma cifra com base na chave
    cipher = Fernet(key)

    # Criptografar a pessoa com a cifra
    encrypted_person = cipher.encrypt(person_dumps)

    return (encrypted_person, key)


def decrypt(encrypted_person: bytes, key: bytes) -> bytes:
    '''
    ### Função
    Descriptografa um conjunto de dados a partir da chave informada como parâmetro.

    A complexidade está intrinsecamente ligada a uma biblioteca externa, cujos detalhes
    não são necessários.
    '''

    # Recuperar a cifra com base na chave
    cipher = Fernet(key)

    # Descriptografar o dado
    decrypted_person = cipher.decrypt(encrypted_person)

    return decrypted_person
