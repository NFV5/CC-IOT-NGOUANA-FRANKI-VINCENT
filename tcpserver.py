import socket
import ssl
# Configuration du serveur
host = 'localhost'
port = 8000
CERTFILE = '/home/ngouana/certificat.pem'
KEYFILE = '/home/ngouana/cle_privee.pem'
# Créer un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration des paramètres de sécurité
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile= CERTFILE, keyfile= KEYFILE)

# Liaison du socket à une adresse et un port
sock.bind((host, port))
sock.listen(1)

# Attente de la connexion d'un client
print("Serveur TCP démarré. En attente de connexions...")
client_sock, client_address = sock.accept()

# Connexion sécurisée avec le client
secure_sock = context.wrap_socket(client_sock, server_side=True)

try:
    # Réception des données du client
    data = secure_sock.recv(1024)
    print("Réponse du serveur:", data.decode())

    # Envoi d'une réponse au client
    response = "Hello, client!"
    secure_sock.sendall(response.encode())
finally:
    # Fermeture de la connexion sécurisée
    secure_sock.close()

# Fermeture du socket
sock.close()