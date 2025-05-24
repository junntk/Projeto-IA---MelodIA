import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Carrega o dataset normalizado
df = pd.read_csv('dataset/spotify_anonimizado.csv')

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
musica_base = "Romantic Homicide"  # Altere para qualquer música do CSV
idx = df_scaled[df_scaled['track_name'] == musica_base].index[0]

# Encontra as 5 músicas mais próximas (exceto ela mesma)
distancias, indices = knn.kneighbors([df_scaled.loc[idx, features]])
print(f"\nRecomendações baseadas na música: {musica_base}\n")

for i in indices[0][1:]:  # pula o primeiro (é a própria música)
    nome = df_scaled.loc[i, 'track_name']
    artista = df_scaled.loc[i, 'artist']
    print(f"- {nome} ({artista})")
