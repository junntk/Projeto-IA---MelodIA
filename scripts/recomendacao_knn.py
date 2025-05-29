"""
Membros do Grupo:
- Kenny Jun Takahashi – RA: 10396373
- Yuri Nichimura Alves – RA: 10401701

Descrição:
Este script implementa o algoritmo de recomendação K-Nearest Neighbors (KNN) com base nas características musicais normalizadas, previamente extraídas da API do Spotify.
As etapas incluem:
- Carregamento do dataset tratado (`spotify_anonimizado.csv`);
- Seleção e padronização das variáveis numéricas utilizadas como features;
- Treinamento do modelo KNN utilizando distância euclidiana;
- Identificação e exibição das músicas mais semelhantes a uma faixa de referência.

Histórico de Atualizações:
- 30/03/2025 – Kenny Jun Takahashi – Implementação inicial do modelo KNN e geração de recomendações.
- 30/03/2025 – Kenny Jun Takahashi – Ajustes na entrada da música base e refinamento da exibição dos resultados.
"""


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Carrega o dataset normalizado
df = pd.read_csv('spotify_anonimizado.csv')

# Seleciona as features numéricas
features = ['danceability', 'energy', 'speechiness', 'acousticness',
            'instrumentalness', 'liveness', 'valence', 'tempo']

# Normaliza os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Recria o DataFrame com os dados normalizados
df_scaled = pd.DataFrame(X_scaled, columns=features)
df_scaled['track_name'] = df['track_name']
df_scaled['artist'] = df['artist']

# Treina o modelo KNN
knn = NearestNeighbors(n_neighbors=6, metric='euclidean')
knn.fit(df_scaled[features])

# Escolhe uma música como base
musica_base = "EASY"  # Altere para qualquer música do CSV
idx = df_scaled[df_scaled['track_name'] == musica_base].index[0]

# Encontra as 5 músicas mais próximas (exceto ela mesma)
entrada = pd.DataFrame([df_scaled.loc[idx, features].values], columns=features)
distancias, indices = knn.kneighbors(entrada)
print(f"\nRecomendações baseadas na música: {musica_base}\n")

for i in indices[0][1:]:  # pula o primeiro (é a própria música)
    nome = df_scaled.loc[i, 'track_name']
    artista = df_scaled.loc[i, 'artist']
    print(f"- {nome} ({artista})")
