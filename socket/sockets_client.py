import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024 # un kilo octot

print(f"connexion au serveur {HOST_IP}, port {HOST_PORT}")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError as e:
        print(f"ERREUR : impossible de se connecter reconnection ....")
        time.sleep(4)
    else:
        print(f"connexion étabie avec")
        break




    data_recues = s.recv(MAX_DATA_SIZE)
    print(data_recues)
    s.close()