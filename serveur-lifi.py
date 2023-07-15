import ssl
import socket

# Créer un objet socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Activer TLS
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="/home/ngouana/certificat.pem", keyfile="/home/ngouana/cle_privee.pem")

# Lier le socket à un hôte et un port 
server_socket.bind(('localhost', 8000))

# Écouter les connexions entrantes
server_socket.listen(1)

# Gérer les connexions entrantes
while True:
    # Accept  connection du client
    client_socket, client_address = server_socket.accept()

    # Enveloppez la prise avec TLS
    secure_client_socket = context.wrap_socket(client_socket, server_side=True)

    #Reception des données du client
    data = secure_client_socket.recv(1024)

    # Traitez les données reçues ici
    # fermer la connexion
    secure_client_socket.close()