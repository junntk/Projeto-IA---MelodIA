"""
Membros do Grupo: 
- Arthur Santos Afonso Ferreira – RA: 10381332
- Ian Theodoro Campanhã – RA: 10381723
- Kenny Jun Takahashi  – RA: 10396373
- Yuri Nichimura Alves - RA: 10401701

Descrição:
Este script realiza a análise exploratória dos dados musicais coletados da API do Spotify.
As etapas incluem:
- Visualização das primeiras linhas do dataset e suas estatísticas descritivas;
- Análise da distribuição das principais características acústicas das músicas por meio de histogramas;
- Avaliação da correlação entre essas características usando mapa de calor (heatmap);
- Normalização das variáveis numéricas com `StandardScaler`, a fim de preparar os dados para futuras análises.

Histórico de Atualizações:
- 27/03/2025 – Arthur Santos Afonso Ferreira – Criação do script de análise com carregamento e visualização dos dados.
- 27/03/2025 – Ian Theodoro – Implementação das visualizações de distribuição e correlação entre as features.
- 28/03/2025 – Yuri Nichimura Alves – Adição do processo de normalização dos dados com StandardScaler.
- 28/03/2025 – Kenny Jun Takahashi – Revisão geral do código.
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

sns.set(style='whitegrid')

#Carrega o dataset
df = pd.read_csv('../dataset/spotify_anonimizado.csv')
print(df.head())

#Estatísticas descritivas
print(df.describe())

#Distribuição das características
features = ['danceability', 'energy', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo']

df[features].hist(bins=15, figsize=(15, 10), color='skyblue', edgecolor='black')
plt.suptitle('Distribuição das características das músicas', fontsize=16)
plt.show()

#Correlação entre as features
plt.figure(figsize=(10, 8))
sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlação entre características das músicas", fontsize=14)
plt.show()

#Normalização dos dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

df_scaled = pd.DataFrame(X_scaled, columns=features)
df_scaled['track_name'] = df['track_name']
print(df_scaled.head())
