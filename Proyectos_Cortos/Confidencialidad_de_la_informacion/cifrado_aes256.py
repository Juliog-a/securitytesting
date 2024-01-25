from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import time

# Ruta de la imagen de entrada y salida
input_image_path = "Introducir_path_aqui"
output_image_path = "Introducir_path_de_salida_y_nombre_de_imagen_aqui"

start_time = time.time()

# Clave secreta de 256 bits (32 bytes)
secret_key = b'EstaEsUnaClaveMuySegura256Bitsx00x01'[:32]

# Inicialización del cifrador AES en modo CBC
cipher = AES.new(secret_key, AES.MODE_CBC)

# Abre la imagen de entrada en modo binario
with open(input_image_path, "rb") as infile:
    plaintext = infile.read()

# Asegura que la longitud del texto plano sea un múltiplo de 16 bytes (bloque AES)
while len(plaintext) % 16 != 0:
    plaintext += b'\x00'

# Cifra el texto plano
ciphertext = cipher.encrypt(plaintext)

# Guarda la clave secreta en un archivo (guárdala de forma segura)
with open("secret_key.bin", "wb") as keyfile:
    keyfile.write(secret_key)

# Guarda la imagen cifrada en un archivo
with open(output_image_path, "wb") as outfile:
    outfile.write(cipher.iv)  # Guarda el vector de inicialización
    outfile.write(ciphertext)

end_time = time.time()
elappsed_time_ms = (end_time - start_time)*1000

print("Imagen cifrada con éxito utilizando AES-256.")
print("Tiempo transcurrido (segundos):")
print(elappsed_time_ms)

