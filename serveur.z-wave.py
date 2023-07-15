from openzwave.network import ZWaveNetwork
# Initialiser le réseau Z-Wave
network = ZWaveNetwork()
# Attendre que le réseau soit prêt
network.start()
print("Serveur Z-Wave démarré")
# Boucle principale du serveur
while True:
# Vérifier les événements Z-Wave
network.update()# Traiter les événements reçus
for node in network.nodes:
for value in network.nodes[node].get_changed_values():
print(f"Node ID: {node} - Value ID: {value.value_id} - Nouvelle
valeur: {value.data}")
# Arrêter le réseau Z-Wave
network.stop()