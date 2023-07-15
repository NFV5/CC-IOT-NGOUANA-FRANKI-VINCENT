import socket
import ssl
# Configuration du client
host = 'localhost'
port = 8000
# Créer un socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configuration des paramètres de sécurité
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile="/home/ngouana/certificat.pem")

# Se connecter au serveur
sock.connect((host , port))

# Connexion sécurisée avec le serveur
secure_sock = context.wrap_socket(sock, server_hostname=host)
print("Connecté au serveur TCP")

try:
    # Envoi de données au serveur
    message = "Hello, server!"
    secure_sock.sendall(message.encode())

    # Réception de la réponse du serveur
    response = secure_sock.recv(1024)
    print("Réponse du serveur:", response.decode())
finally:
    # Fermeture de la connexion sécurisée
    secure_sock.close()

# Fermeture du socket
sock.close()
