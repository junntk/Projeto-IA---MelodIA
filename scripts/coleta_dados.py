"""
Membros do Grupo: 
- Arthur Santos Afonso Ferreira – RA: 10381332
- Ian Theodoro Campanhã – RA: 10381723
- Kenny Jun Takahashi  – RA: 10396373
- Yuri Nichimura Alves - RA: 10401701

Descrição:
Este script realiza a autenticação via API do Spotify e coleta informações das músicas salvas pelo usuário. 
Para cada faixa, são extraídas características acústicas relevantes utilizando a função `audio_features`, 
tais como dançabilidade, energia, discurso, acústica, instrumentalidade, vivacidade, valência e tempo (BPM). 
Os dados são organizados em um DataFrame do Pandas, anonimizados por meio de um identificador derivado do hash da faixa,e exportados para um arquivo CSV localizado em 'dataset/spotify_anonimizado.csv'.

Histórico de Atualizações:
- 23/03/2025 – Arthur Santos Afonso Ferreira – Criação do script com autenticação e coleta básica de dados.
- 23/03/2025 – Arthur Santos Afonso Ferreira – Inclusão de extração de atributos acústicos e anonimização do identificador do usuário.
- 24/03/2025 – Arthur Santos Afonso Ferreira – Tratamento de exceções e exportação dos dados em formato CSV para o diretório apropriado.
"""



import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time

#Configuração de autenticação
CLIENT_ID = "SEU_CLIENT_ID"
CLIENT_SECRET = "SEU_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8888/callback"

#Escopo
SCOPE = "user-library-read user-top-read"

#Autenticação
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

#Coleta de dados
print("Coletando músicas salvas do usuário...")
results = sp.current_user_saved_tracks(limit=50)

tracks_data = []

for item in results['items']:
    track = item['track']
    track_id = track['id']
    try:
        features = sp.audio_features(track_id)[0]
        if features:
            tracks_data.append({
                "track_id": track_id,
                "track_name": track['name'],
                "artist": track['artists'][0]['name'],
                "duration_ms": track['duration_ms'],
                "danceability": features['danceability'],
                "energy": features['energy'],
                "speechiness": features['speechiness'],
                "acousticness": features['acousticness'],
                "instrumentalness": features['instrumentalness'],
                "liveness": features['liveness'],
                "valence": features['valence'],
                "tempo": features['tempo'],
                "user_anon_id": f"user_{hash(track_id) % 1000}"
            })
        time.sleep(0.1)
    except Exception as e:
        print(f"Erro com {track['name']}: {e}")

df = pd.DataFrame(tracks_data)
df.to_csv("dataset/spotify_anonimizado.csv", index=False)
print("Arquivo salvo como 'dataset/spotify_anonimizado.csv'")
