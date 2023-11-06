import random

clients = []

for _ in range(50):
    nom = f"Client {random.randint(1, 1000)}"
    email = f"client{random.randint(1000, 9999)}@example.com"
    montant_depense = round(random.uniform(100, 1000), 2)

    client = {
        "nom": nom,
        "email": email,
        "montant_depense": montant_depense
    }

    clients.append(client)

for i, client in enumerate(clients, start=1):
    print(f"Client {i}:")
    print(f"Nom: {client['nom']}")
    print(f"Email: {client['email']}")
    print(f"Montant dépensé: {client['montant_depense']}")
    print()
