import streamlit as st
import psutil
import os
import time

process = psutil.Process(os.getpid())

while True:
    # Afficher l'utilisation de la mémoire
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Convertir en Mo
    st.write(f"Utilisation de la mémoire: {memory_usage:.2f} Mo")

    # Afficher l'utilisation du CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    st.write(f"Utilisation du CPU: {cpu_usage:.2f}%")

    # Mettre à jour toutes les 5 secondes
    time.sleep(5)