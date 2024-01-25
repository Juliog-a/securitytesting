from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import os
import base64

# Genera una clave maestra a partir de una contraseña y sal
def generar_clave_maestra(contrasena, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # Ajusta el número de iteraciones según sea necesario
        salt=salt,
        length=32  # Longitud de la clave maestra
    )

    clave_maestra = base64.urlsafe_b64encode(kdf.derive(contrasena))
    return clave_maestra

# Almacena la clave maestra en un archivo
def almacenar_clave_maestra(clave_maestra, archivo_clave_maestra):
    with open(archivo_clave_maestra, 'wb') as file:
        file.write(clave_maestra)

# Lee la clave maestra desde el archivo
def leer_clave_maestra(archivo_clave_maestra):
    with open(archivo_clave_maestra, 'rb') as file:
        return file.read()

# Cifra un archivo de imagen
def cifrar_archivo(clave, archivo_entrada, archivo_salida):
    f = Fernet(clave)
    with open(archivo_entrada, 'rb') as file:
        data = file.read()
        data_cifrado = f.encrypt(data)
    with open(archivo_salida, 'wb') as file:
        file.write(data_cifrado)

# Descifra un archivo de imagen
def descifrar_archivo(clave, archivo_entrada, archivo_salida):
    f = Fernet(clave)
    with open(archivo_entrada, 'rb') as file:
        data_cifrado = file.read()
        data_descifrado = f.decrypt(data_cifrado)
    with open(archivo_salida, 'wb') as file:
        file.write(data_descifrado)

# MAIN
if __name__ == '__main__':
    contrasena = b'ContrasenaSuperSegura'  # Cambiar esto por una contraseña realmente segura
    salt = os.urandom(16)  # Genera una sal aleatoria

    clave_maestra = generar_clave_maestra(contrasena, salt)
    archivo_clave_maestra = 'clave_maestra.key'
    almacenar_clave_maestra(clave_maestra, archivo_clave_maestra)

    archivo_entrada = 'imagen_prueba.jpg'
    archivo_cifrado = 'imagen_prueba_cifrada.jpg'
    archivo_descifrado = 'imagen_prueba_descifrada.jpg'

    cifrar_archivo(clave_maestra, archivo_entrada, archivo_cifrado)

    descifrar_archivo(clave_maestra, archivo_cifrado, archivo_descifrado)
    print("Archivo cifrado y descifrado con éxito!")
