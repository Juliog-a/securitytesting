from Cryptodome.Cipher import AES
import time

# Ruta de la imagen cifrada y salida
input_image_path = "Introducir_path_aqui"
output_image_path = "Introducir_path_de_salida_y_nombre_de_imagen_aqui"

start_time = time.time()

# Ruta del archivo de clave secreta y el IV
secret_key_path = "Introducir_path_secret_key/secret_key.bin"

# Lee el vector de inicialización (IV) y la clave secreta desde los archivos
with open(secret_key_path, "rb") as keyfile:
    secret_key = keyfile.read()

with open(input_image_path, "rb") as infile:
    iv = infile.read(16)  # Lee los primeros 16 bytes como IV
    ciphertext = infile.read()

# Inicialización del cifrador AES en modo CBC
cipher = AES.new(secret_key, AES.MODE_CBC, iv)

# Descifra el texto cifrado
plaintext = cipher.decrypt(ciphertext)

# Guarda la imagen descifrada en un archivo
with open(output_image_path, "wb") as outfile:
    outfile.write(plaintext)

end_time = time.time()
elappsed_time_ms = (end_time - start_time)*1000

print("Imagen descifrada con éxito.")
print("Tiempo transcurrido (segundos):")
print(elappsed_time_ms)
