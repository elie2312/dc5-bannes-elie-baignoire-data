import random

clients = []

for _ in range(50):
    nom = f"Client {random.randint(1, 1000)}"
    email = f"client{random.randint(1000, 9999)}@example.com"
    montant_depense = round(random.uniform(50, 500), 2)

    client = {
        "nom": nom,
        "email": email,
        "montant_depense": montant_depense
    }

    clients.append(client)

def montant_total_depense(clients):
    total = 0
    for client in clients:
        total += client["montant_depense"]
    return total

clients = [
    {"nom": "Client 1", "email": "client1@example.com", "montant_depense": 500},
    {"nom": "Client 2", "email": "client2@example.com", "montant_depense": 700},
]

total_depense = montant_total_depense(clients)

print("Montant total dépensé par tous les clients :", total_depense)
