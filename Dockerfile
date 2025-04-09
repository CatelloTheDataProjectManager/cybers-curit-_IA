# Utiliser une image Python 3.12 de base
FROM python:3.12-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY main.py .
COPY encrypt_clients.py .
COPY decrypt_clients.py .
COPY clients.csv .
COPY key.key .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Spécifier la commande par défaut pour exécuter le script Python
CMD ["python", "main.py"]