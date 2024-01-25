import socket


def clientSocket(HOST, PORT, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(message)
        data = s.recv(1024)
        
    print(f"Received {data!r}")
  
