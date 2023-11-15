import socket
import ssl

# Paramètres du client
HOST = '127.0.0.1'
PORT = 12345
CERT_FILE = 'server.crt'

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Établir la connexion sécurisée avec TLS
ssl_socket = ssl.wrap_socket(client_socket, ca_certs=CERT_FILE, cert_reqs=ssl.CERT_REQUIRED)
ssl_socket.connect((HOST, PORT))

print(f"Connexion sécurisée établie avec {HOST}:{PORT}")

# Envoyer des messages au serveur
while True:
    message = input("Saisissez un message (ou 'exit' pour quitter) : ")
    ssl_socket.sendall(message.encode('utf-8'))
    if message.lower() == 'exit':
        break

# Fermer la connexion
ssl_socket.close()