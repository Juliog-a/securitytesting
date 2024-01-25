VERIFICADORES DE INTEGRIDAD EN LA TRANSMISIÓN PUNTO-PUNTO

## Archivo main.py:
  Este archivo es el punto de entrada principal de este proyecto. Aquí se encuentra la lógica principal
  que permite configurar y ejecutar tanto el cliente como el servider del sistema. A continuación, se proporciona
  una descripción de lo que hace este archivo:

  -- Configuración del sistema de logs: Se configura un sistema de registro que almacena los eventos importantes
      del programa en el archivo  **mi_programa.log** para facilitar el seguimiento y la depuración del programa
  
  -- Lógica Principal: Elección de configuración como cliente o servidor

  -- Registro de Eventos: durante la ejecución del programa, se registran eventos como la configuración del cliente
      o servidor, mensajes enviados y eventos de prueba.

## Archivo descifrado_mensaje.py:
  Este módulo contiene funciones para encriptar y desencriptar mensajes.
  
  **create_msg(msj, clave_str, nonce)**: Esta función recibe un mensaje una clave y un nonce como entrada
    y los combina en un diccionario. Luego, convierte el diccionario en una cadena JSON y la devuelve como 
    resultado.
      
  **received_msg(decrypt_msg)**: Recibe un mensaje descifrado en formato JSON y lo convierte en un diccionario. 
    Luego, extrae y devuelve el mensaje, la clave y el nonce del diccionario.
    
  **generate_nonce()**: Genera un nonce aleatorio de 32 bytes y lo devuelve.
    
  **messageEncrypt(msg, clave)**: Utiliza la clave proporcionada para encriptar un mensaje. Genera un nonce 
    aleatorio, crea un mensaje en formato JSON que incluye el mensaje, la clave y el nonce, y luego encripta 
    este mensaje utilizando Fernet. Devuelve el mensaje encriptado.
  **messageDecrypt(codedMessage, clave)**: Recibe un mensaje encriptado y la clave utilizada para encriptarlo. 
    Desencripta el mensaje, registra el mensaje desencriptado en el sistema de logs y lo convierte en un 
    diccionario. Luego, devuelve el diccionario que contiene el mensaje desencriptado, la clave y el nonce.

## Archivo noncestore.py:
  Permite almacenar y comprobar nonces:
  **nonceStore(nonce)**: Esta función recibe un nonce como parámetro y lo almacena en el archivo **nonce.txt**. 
    El archivo es utilizado para llevar un registro de los nonces previamente utilizados.

  **previous_nonces()**: Esta función lee el archivo **nonce.txt** y extrae los nonces almacenados previamente. 
    
  **check_nonce(pre_nonces, nonce)**: Comprueba si un nonce dado ya ha sido almacenado previamente en el archivo 
    **nonce.txt**. Si el nonce ya se encuentra en la lista de nonces previamente almacenados, se registra un 
    error y se devuelve un mensaje de error. Si el nonce no se encuentra en la lista, se registra la comprobación 
    y se almacena el nonce en el archivo antes de devolver un mensaje de éxito.
    
## Archivo clientsocket.py:
  Crea un socket, se conecta al host y puerto especificados y envía el mensaje al servidor. Luego, espera una 
  respuesta del servidor y la imprime en la consola.

## Archivo serversocket.py:
  Permite configurar un servidor para recibir mensajes encriptados desde un cliente. Crea un socket, 
  lo enlaza al host y puerto especificados, y luego escucha las conexiones entrantes. Cuando se establece una 
  conexión con un cliente, se desencripta el mensaje recibido y se realizan comprobaciones de seguridad. 
  Dependiendo de los resultados de estas comprobaciones, se envía una respuesta al cliente. Las comprobaciones 
  incluyen la verificación del nonce y la detección de tokens no válidos.

## Archivo tests.py:
  Este archivo contiene funciones que premiten realizar diferentes pruebas en el sistema de encriptado.
  Las pruebas se centrar en comprobar la funcionalidad del sistema en situaciones específicas basadas en los 
  posibles ataques de un man-in-the-middle.
  
  **test_normal_msg(msg, clave)**: Encripta un mensaje utilizando la clave proporcionada.
  
  **test_nonce_repetition(msg, clave)**: Realiza una prueba de repetición enviando mensajes con el nonce 
    predefinido.
  
  **test_change_messageEncryot(msg, clave)**: Modifica el mensaje durante el envio para provocar un error de
    desencriptado.


