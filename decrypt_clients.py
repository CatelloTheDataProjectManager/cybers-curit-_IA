from cryptography.fernet import Fernet
import csv

# Charger la clé de chiffrement existante depuis le fichier key.key
with open("key.key", "rb") as key_file:
    key = key_file.read()
cipher_suite = Fernet(key)

# Fonction pour déchiffrer les données
def decrypt_data(data):
    return cipher_suite.decrypt(data.encode()).decode()

# Lire et déchiffrer les données du fichier clients_encrypted.csv
decrypted_data = []
with open("clients_encrypted.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        decrypted_row = {
            "ID": decrypt_data(row["ID"]),
            "Nom": decrypt_data(row["Nom"]),
            "Email": decrypt_data(row["Email"]),
            "Téléphone": decrypt_data(row["Téléphone"]),
            "Commentaire": row["Commentaire"],  # Les commentaires restent inchangés
        }
        decrypted_data.append(decrypted_row)

# Écrire les données déchiffrées dans un nouveau fichier CSV
with open("clients_decrypted.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["ID", "Nom", "Email", "Téléphone", "Commentaire"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(decrypted_data)

print("Les données ont été déchiffrées et enregistrées dans 'clients_decrypted.csv'.")