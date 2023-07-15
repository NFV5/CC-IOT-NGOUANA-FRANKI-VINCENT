import ssl
import socket

# Activation de TLS
context = ssl.create_default_context()

# Connect to the server
with socket.create_connection(('localhost', 8000)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname='localhost') as secure_client_socket:
        # Envoie des données au serveur
        secure_client_socket.sendall(b'Hello, world!')

        # Reception des données du serveur
        data = secure_client_socket.recv(1024)

        # Traitez les données reçues 