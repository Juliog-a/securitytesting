import logging

def nonceStore(nonce):
    with open('nonce.txt', 'a') as file:
        file.write(str(nonce) + ",")

def previous_nonces():
    try:
        with open('nonce.txt', 'r') as file:
            pre_nonces = [elemento.strip() for line in file for elemento in line.split(',')]
        return pre_nonces
    except FileNotFoundError:
        return []


def check_nonce(pre_nonces, nonce):
    logging.info("nuesto nonce: {}".format(nonce))
    print("Nonces almacenados", pre_nonces)
    if nonce in pre_nonces:
        logging.info("Error producido: Se ha repetido el nonce")
        msj = "Nonce repetido, ERROR"
        return msj
    else:
        logging.info("Check: Nonce no repetido")
        msj = "El nonce no está repetido"
        nonceStore(nonce) #almacenamos el nonce en el archivo
        return msj


    