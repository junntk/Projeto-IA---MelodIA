# MelodIA: Um sistema de recomendação de músicas baseado nos gostos dos usuários

Integrantes 
- Kenny Jun Takahashi  – RA: 10396373
- Yuri Nichimura Alves - RA: 10401701


Este projeto tem como objetivo desenvolver um sistema de recomendação de músicas utilizando técnicas de Machine Learning e dados obtidos por meio da API oficial do Spotify.

---

## Coleta e Análise Exploratória dos Dados

### Dataset Utilizado

O arquivo `spotify_anonimizado.csv` foi gerado a partir das músicas salvas por um usuário em sua biblioteca do Spotify, por meio da API. As seguintes características musicais foram extraídas:

- `track_name`: Nome da música  
- `artist`: Nome do artista   
- `danceability`: Grau de dançabilidade da música  
- `energy`: Intensidade percebida da faixa  
- `speechiness`: Presença de palavras faladas  
- `acousticness`: Probabilidade de a música ser acústica  
- `instrumentalness`: Presença de instrumentos  
- `liveness`: Indicação de performance ao vivo  
- `valence`: Grau de positividade emocional  
- `tempo`: BPM (batidas por minuto)  


Observação: Nenhuma informação pessoal foi mantida no dataset. Todos os dados foram devidamente anonimizados.

### Análise Exploratória

A análise exploratória foi realizada com base nos seguintes arquivos:

- `scripts/analise_dados.py`: Versão em script com análise estatística e visualizações  

As principais atividades desenvolvidas foram:

- Visualização das primeiras linhas do dataset  
- Cálculo de estatísticas descritivas  
- Análise gráfica da distribuição das características musicais  
- Análise de correlação entre as variáveis  
- Normalização dos dados com `StandardScaler`  

---

## Estrutura dos Scripts

- `scripts/coleta_dados.py`: Script responsável pela autenticação e extração dos dados via API do Spotify  
- `scripts/analise_dados.py`: Script contendo a análise exploratória dos dados
- `scripts/recomendacao_knn.py`: Script que implementa o algoritmo K-Nearest Neighbors (KNN) para gerar recomendações de músicas com base em similaridade acústica.
- `dataset/spotify_anonimizado.csv`: Arquivo CSV contendo os dados extraídos e tratados
  

---

## Sistema de Recomendação com Machine Learning

Nesta segunda etapa do projeto, foi implementado um sistema de recomendação utilizando o algoritmo K-Nearest Neighbors (KNN), que sugere músicas com base na similaridade entre suas características sonoras.
