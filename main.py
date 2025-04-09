import csv
import pandas as pd
from transformers import pipeline
import time
import streamlit as st
from datetime import datetime

# Dictionnaire pour stocker les informations d'identification des utilisateurs
users = {
    "user1": {"password": "password1", "file": "clients_encrypted.csv"},
    "user2": {"password": "password2", "file": "clients_decrypted.csv"}
}

# Fichier de journalisation
log_file = "user_log.csv"

def log_user_activity(username, status):
    """Enregistre les tentatives de connexion des utilisateurs."""
    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, username, status])

def authenticate(username, password):
    if username in users and users[username]["password"] == password:
        log_user_activity(username, "Success")
        return users[username]["file"]
    log_user_activity(username, "Failed")
    return None

def analyze_sentiments(file_path, model_path):
    try:
        # Initialiser le pipeline d'analyse des sentiments
        classifier = pipeline("sentiment-analysis", model=model_path)

        # Lire le fichier CSV
        with open(file_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            results = []

            # Suivi des performances
            start_time = time.time()

            # Analyser chaque commentaire dans le champ "Commentaire"
            for row in reader:
                commentaire = row['Commentaire']
                sentiment_result = classifier(commentaire)
                results.append({
                    'Nom': row['Nom'],
                    'Email': row['Email'],
                    'Téléphone': row['Téléphone'],
                    'Commentaire': commentaire,
                    'Sentiment': sentiment_result[0]['label'],
                    'Score': sentiment_result[0]['score']
                })

            # Calculer les performances
            end_time = time.time()
            total_time = end_time - start_time
            st.write(f"Temps total d'analyse : {total_time:.2f} secondes")

        # Convertir les résultats en DataFrame
        df = pd.DataFrame(results)

        # Afficher le DataFrame dans Streamlit
        st.dataframe(df)

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    st.title("Analyse des Sentiments")

    # Utiliser st.session_state pour conserver l'état de connexion
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.file_path = None

    # Authentification utilisateur
    if not st.session_state.authenticated:
        username = st.text_input("Nom d'utilisateur :")
        password = st.text_input("Mot de passe :", type="password")

        if st.button("Se connecter"):
            file_path = authenticate(username, password)
            if file_path:
                st.session_state.authenticated = True
                st.session_state.file_path = file_path
                st.success(f"Connecté en tant que {username}")
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect")
    else:
        st.success(f"Connecté")
        local_model_path = st.text_input("Chemin du modèle local :", "model/distilbert")
        if st.button("Lancer l'analyse"):
            analyze_sentiments(st.session_state.file_path, local_model_path)
