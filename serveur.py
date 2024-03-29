import socket
import ssl

# Paramètres du serveur
HOST = '127.0.0.1'
PORT = 12345
CERT_FILE = 'server.crt'
KEY_FILE = 'server.key'

# Création du socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serveur en attente de connexion sur {HOST}:{PORT}")

# Accepter la connexion sécurisée avec TLS
client_socket, client_address = server_socket.accept()
ssl_socket = ssl.wrap_socket(client_socket, keyfile=KEY_FILE, certfile=CERT_FILE, server_side=True, cert_reqs=ssl.CERT_REQUIRED)

print(f"Connexion sécurisée établie avec {client_address}")

# Attendre et afficher les messages du client
while True:
    data = ssl_socket.recv(1024)
    if not data:
        break
    print(f"Message du client: {data.decode('utf-8')}")

# Fermer les connexions
ssl_socket.close()
server_socket.close()