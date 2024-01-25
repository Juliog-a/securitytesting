import socket
import descifrado_mensaje
import noncestore
from cryptography.fernet import InvalidToken
import logging


def socket_server(HOST, PORT,clave):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    try: 
                        decrypted_data = descifrado_mensaje.messageDecrypt(data,clave) #diccionario
                        received_message = decrypted_data["mensaje"]
                        received_nonce = decrypted_data["nonce"]

                        logging.info(f"Mensaje recibido en el servidor una vez desencriptado: {received_message}\n")
                        logging.info(f"Nonce recibido en el servidor una vez desencriptado: {received_nonce} \n")


                        #comprobación del NONCE:
                        #Obtenemos todos los nonces anteriores:
                        stored_nonces = noncestore.previous_nonces()
                        
                        #Comprobamos si el nonce recibido ya ha sido almacenado:
                        msj_nonce = noncestore.check_nonce(stored_nonces, received_nonce)

                        #Si no ha ocurrido ningún error, mandamos un mensaje de transacción correcta

                        if msj_nonce != "El nonce no está repetido":
                            logging.info(f"Resultado de transacción: {msj_nonce}")
                            conn.send(msj_nonce.encode())
                        else:
                            msj = "Transaccion realizada con exito!"
                            logging.info(f"Resultado de transacción: {msj}")
                            conn.send(msj.encode())
                        '''
                        if InvalidToken:
                            msj = "ERROR: token no valido, no se puede desencriptar el mensaje"
                            logging.info(f"Resultado de transacción: {msj}")
                            conn.send(msj.encode())
                        '''

                        
                            
                    except InvalidToken:
                        msj = "ERROR: token no valido, no se puede desencriptar el mensaje"
                        logging.info(f"Resultado de transacción: {msj}")
                        conn.send(msj.encode())
                    except Exception as e:
                        msj = f"Ocurrio un error inesperado: {str(e)}"
                        logging.info(f"Resultado de transacción: {msj}")
                        conn.send(msj.encode())

                    

                    

                    




                               
          