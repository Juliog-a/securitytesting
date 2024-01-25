import serversocket
import tests
import clientsocket
import logging


# Configuración del sistema de logs
logging.basicConfig(filename='mi_programa.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Hemos utilizado una clave estática suponiendo que la clave se estableció en el HandShake entre cliente y servidor.
# La clave cumple con los requisitos de seguridad establecidos.
clave_str = "gDS8M8F5naD0ukJGZXnKNwouc6uppMxBrIXaSna8FxY="

if __name__ == "__main__":
    decision1 = input("¿Desea configurar el Servidor (S) o el Cliente (C)?: ") #decisión del usuario
    if decision1 == "C":
        #port = input("Inserte puerto: ")    #puerto a escuchar
        #host = input("Inserte host: ")      #host a conectar
        #msg = input("Inserte mensaje: ")    #mensaje a enviar

        port = 8080
        host = "localhost"
        msg = "Más pruebas"
        logging.info(f"Mensaje que envia el cliente: {msg} ")
        logging.info(f"Configurando el cliente en el puerto {port} y host {host}")
        logging.info("___________ Ejecutando Tests _________") #Test1 = normal, Test2 = nonce_x2, Test3 = mensaje modificado
        
        enc_msg = tests.tests(msg, clave_str)
        clientsocket.clientSocket(host, int(port), enc_msg) #enviar mensaje
   
       
    elif decision1 == "S":
       # port = input("Inserte puerto: ") #puerto a escuchar
        #host = input("Inserte host: ") #host a conectar 
        port = 8080
        host = "localhost"
        logging.info(f"Configurando el servidor en el puerto {port} y host {host}")
        serversocket.socket_server(host, int(port), clave_str.encode()) #escuchar mensaje
    else: 
        print ("No ha elegido una opción correcta, cerrando sesión...")
        logging.error("Opción no válida, Sesion cerrada.")

