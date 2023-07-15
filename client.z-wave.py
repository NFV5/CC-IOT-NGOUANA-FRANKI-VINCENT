from openzwave.network import ZWaveNetwork
from openzwave.value import ZWaveValue
# Initialiser le réseau Z-Wave
network = ZWaveNetwork()
# Attendre que le réseau soit prêt
network.start()
print("Client Z-Wave démarré")
# Identifier le nœud cible (remplacer le node_id par l'ID du nœud Z-Wave
souhaité)
node_id = 2
# Récupérer les informations de nœud
node = network.nodes[node_id]
# Vérifier si le nœud est prêt à être utilisé
if node.is_ready:
# Obtenir toutes les valeurs du nœud
values = node.get_values()
# Parcourir les valeurs du nœud
for value_id, value in values.items():
# Vérifier si la valeur est lisible
if value.is_read_only():
# Lire la valeur
value.refresh()
print(f"Node ID: {node_id} - Value ID: {value_id} - Valeur
actuelle: {value.data}")# Arrêter le réseau Z-Wave
network.stop()