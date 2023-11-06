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

for client in clients:
    if client["montant_depense"] > 100:
        print(f"Nom: {client['nom']}")
        print(f"Email: {client['email']}")
        print(f"Montant dépensé: {client['montant_depense']}")
        print()
