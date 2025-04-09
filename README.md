# Sentiment Analysis 📊🤖

This project is a sentiment analysis application developed with Streamlit. It allows users to log in, access their client comment files, and analyze the sentiments expressed in these comments using a natural language processing (NLP) model.

## Features ✨

- **User Authentication**: Users must authenticate to access their comment files.
- **Activity Logging**: Login attempts are recorded in a log file.
- **Sentiment Analysis**: Uses an NLP model to analyze sentiments in client comments.
- **User Interface**: Intuitive interface developed with Streamlit for interacting with the application.
- **Data Encryption and Decryption**: Sensitive client data is encrypted for security and can be decrypted for analysis.

## Prerequisites 🛠️

- Python 3.x
- Python Libraries: `csv`, `pandas`, `transformers`, `time`, `streamlit`, `datetime`, `cryptography`

## Usage 🚀

1. Launch the Streamlit application.
2. Open the application in your web browser.
3. Log in with your credentials.
4. Enter the local model path and start the sentiment analysis.
5. Encrypt sensitive data before saving and decrypt it when needed for analysis.

## Project Structure 📂

- Main file containing the application logic.
- `user_log.csv`: Log file for recording login attempts.
- `key.key`: Encryption key file for secure data storage.
- `clients_encrypted.csv`: Encrypted client data file.
- `clients_decrypted.csv`: Decrypted client data file for analysis.

## Encryption and Decryption 🔐

- **Encryption**: Sensitive client data is encrypted using the `cryptography` library and stored in `clients_encrypted.csv`.
- **Decryption**: Encrypted data is decrypted for analysis and saved in `clients_decrypted.csv`.

## Docker and Kubernetes Integration 🐳☸️

- **Docker**: The application can be containerized using Docker, allowing it to run on any machine with Docker installed.
- **Docker Hub**: The Docker image can be pushed to Docker Hub for easy deployment and sharing.
- **Kubernetes**: Use Kubernetes to orchestrate multiple instances of the application, ensuring scalability and reliability.

## API Development 🌐

Design an API with multiple functionalities, such as user authentication, sentiment analysis, and data encryption/decryption, to extend the application's capabilities.

Perspective: Explore integrating machine learning models for enhanced sentiment analysis and real-time data processing.
