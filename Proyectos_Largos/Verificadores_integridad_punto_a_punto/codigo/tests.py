from cryptography.fernet import Fernet
import descifrado_mensaje
import logging

#archivo de prueba

#Establecemos un nonce no autogenerado (útil para test de repetición)
nonce_str =  "gDS8M8F5naD0ukJGZXnKNwouc6uppMxBrIXaSna8FxZ=" 

def test_normal_msg(msg, clave):
    enc_msg = descifrado_mensaje.messageEncrypt(msg, clave) #mensaje encriptado
    return enc_msg

#repetición del nonce --> envia mensajes con el nonce predefinido
def test_nonce_repetition(msg, clave):
    fernet = Fernet(clave)
    nonce = nonce_str.encode()
    msg_to_code = descifrado_mensaje.create_msg(msg, clave, nonce)
    enc_msg = fernet.encrypt(msg_to_code.encode())
    return enc_msg

#modificamos el mensaje en el camino del envio para provocar un error de desencriptado
def test_change_messageEncrypt(msg, clave):
    enc_original_msg = descifrado_mensaje.messageEncrypt(msg, clave) #mensaje encriptado
    extra_msg = "FORCE_ERROR"
    extra_msg_enc = extra_msg.encode()
    
    logging.info(f"Cadena que se va a añadir al mensaje: {extra_msg}")

    inject_pos = len(enc_original_msg) // 2

    part1 = enc_original_msg[:inject_pos]
    part2 = enc_original_msg[inject_pos:]
    
    enc_msg  = part1 + extra_msg_enc + part2
    return enc_msg

def tests(msg, clave):
    decision3 = input("Elija uno de los test: Envío normal (N),\n Repetición del nonce (R),\n Modificación del mensaje (M)\n")
    if decision3 == "N":
        print("Test1: Envío normal del mensaje \n")
        logging.info("Se está ejecutando el TEST 1")
        return test_normal_msg(msg, clave)
    elif decision3 == "R":
        print("Test2: Repetición del nonce (ejecutar dos veces para nonce duplicado) \n")
        logging.info("Se está ejecutando el TEST 1")
        return test_nonce_repetition(msg, clave)
    elif decision3 == "M":
        print("Test3: Envío de un mensaje modificado, termina con InvalidToken \n")
        logging.info("Se está ejecutando el TEST 3")
        return test_change_messageEncrypt(msg, clave)
    else:
        logging.info("No se eligio ninguna de las opciones validas")
        print("Opción no válida")
