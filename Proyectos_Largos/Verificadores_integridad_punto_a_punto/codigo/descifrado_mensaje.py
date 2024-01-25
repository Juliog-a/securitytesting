from cryptography.fernet import Fernet
import json
import logging

 
#recibe un mensaje y lo devuelve con la clave y el nonce
def create_msg(msj, clave_str, nonce):
    nonce_str = nonce.decode() #Convierte el nonce a str para incluirlo en el diccionario
    #clave_str = clave.decode() #Convierte la clave a str para incluirlo en el diccionario ---> la clave que recibe ya es string
    mensaje_original = {
        "mensaje": msj,
        "clave": clave_str,
        "nonce": nonce_str
    }

    mensaje_json = json.dumps(mensaje_original)
    
    return mensaje_json


def received_msg(decrypt_msg):
    received_msg = json.loads(decrypt_msg.decode())
    res = {
        "mensaje": received_msg["mensaje"],
        "clave": received_msg["clave"],
        "nonce": received_msg["nonce"]
    }
    return res


def generate_nonce():
    nonce_al = Fernet.generate_key() #Genera un nonce aleatorio (32 bytes)
    return nonce_al

def messageEncrypt(msg,clave):
    fernet = Fernet(clave)
    nonce = generate_nonce()
    msg_to_code = create_msg(msg, clave, nonce)
    coded_msg = fernet.encrypt(msg_to_code.encode())
    return coded_msg


def messageDecrypt(codedMessage,clave):
    fernet = Fernet(clave)
    decryptedMessage = fernet.decrypt(codedMessage) # Descifra el mensaje
    logging.info(f"Mensaje desencriptado {decryptedMessage} \n")
    dicc_receivedd = received_msg(decryptedMessage) # Convierte el mensaje descifrado de JSON a un diccionario
    return dicc_receivedd