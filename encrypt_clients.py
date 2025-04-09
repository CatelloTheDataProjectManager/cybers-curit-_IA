from cryptography.fernet import Fernet
import csv

# Charger ou générer une clé de chiffrement
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Sauvegarder la clé dans un fichier pour déchiffrement ultérieur
with open("key.key", "wb") as key_file:
    key_file.write(key)

# Chiffrement des données
def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()

# Lire le fichier clients.csv et chiffrer les données sensibles
encrypted_data = []
with open("clients.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        encrypted_row = {
            "ID": encrypt_data(row.get("ID", "Nouveau")),  # Si pas d'ID, on en génère un
            "Nom": encrypt_data(row["Nom"]),
            "Email": encrypt_data(row["Email"]),
            "Téléphone": encrypt_data(row["Téléphone"]),
            "Commentaire": row["Commentaire"],  # Les commentaires restent en clair dans cet exemple
        }
        encrypted_data.append(encrypted_row)

# Écrire les données chiffrées dans un nouveau fichier CSV
with open("clients_encrypted.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["ID", "Nom", "Email", "Téléphone", "Commentaire"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(encrypted_data)

print("Les données ont été chiffrées et enregistrées dans 'clients_encrypted.csv'.")