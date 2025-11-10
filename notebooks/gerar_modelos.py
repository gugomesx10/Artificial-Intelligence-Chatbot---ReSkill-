"""
Script para gerar modelos pré-treinados para o ReSkill+
Execute este script para criar os arquivos .pickle necessários para a API
"""

import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Carregar dados
print("Carregando dados...")
df_perfil = pd.read_csv('../data/perfil_trabalhador.csv')
df_risco = pd.read_csv('../data/risco_automacao.csv')

# ============================================
# MODELO DE CLASSIFICAÇÃO
# ============================================
print("\nTreinando modelo de classificação...")

# Preparar dados
le_escolaridade = LabelEncoder()
le_area = LabelEncoder()
le_setor = LabelEncoder()
le_perfil = LabelEncoder()

df_perfil['escolaridade_enc'] = le_escolaridade.fit_transform(df_perfil['escolaridade'])
df_perfil['area_atuacao_enc'] = le_area.fit_transform(df_perfil['area_atuacao'])
df_perfil['setor_industria_enc'] = le_setor.fit_transform(df_perfil['setor_industria'])
df_perfil['perfil_enc'] = le_perfil.fit_transform(df_perfil['perfil'])

X_class = df_perfil[['idade', 'escolaridade_enc', 'anos_experiencia', 'area_atuacao_enc', 
                      'habilidades_digitais', 'renda_mensal', 'setor_industria_enc']]
y_class = df_perfil['perfil_enc']

# Treinar modelo
rf_classifier = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)
rf_classifier.fit(X_class, y_class)

# ============================================
# MODELO DE REGRESSÃO
# ============================================
print("Treinando modelo de regressão...")

X_reg = df_risco[['repetitividade', 'criatividade_requerida', 'interacao_humana', 
                   'complexidade_tecnica', 'nivel_educacao']]
y_reg = df_risco['risco_automacao']

# Treinar modelo
gb_regressor = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)
gb_regressor.fit(X_reg, y_reg)

# ============================================
# MODELO DE CLUSTERING
# ============================================
print("Treinando modelo de clustering...")

df_cluster = df_perfil.merge(df_risco[['id', 'risco_automacao']], on='id', how='left')
X_cluster = df_cluster[['idade', 'anos_experiencia', 'habilidades_digitais', 
                        'renda_mensal', 'risco_automacao']].fillna(50)

scaler_cluster = StandardScaler()
X_cluster_scaled = scaler_cluster.fit_transform(X_cluster)

# Treinar modelo
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(X_cluster_scaled)

# ============================================
# SALVAR MODELOS
# ============================================
print("\nSalvando modelos...")

# Criar diretório
import os
os.makedirs('../models', exist_ok=True)

# Salvar classificador
with open('../models/classificador_perfil.pickle', 'wb') as f:
    pickle.dump(rf_classifier, f)
print("✓ classificador_perfil.pickle")

# Salvar regressor
with open('../models/regressor_risco.pickle', 'wb') as f:
    pickle.dump(gb_regressor, f)
print("✓ regressor_risco.pickle")

# Salvar clustering
with open('../models/clustering_kmeans.pickle', 'wb') as f:
    pickle.dump(kmeans, f)
print("✓ clustering_kmeans.pickle")

# Salvar encoders
encoders = {
    'le_escolaridade': le_escolaridade,
    'le_area': le_area,
    'le_setor': le_setor,
    'le_perfil': le_perfil
}
with open('../models/encoders.pickle', 'wb') as f:
    pickle.dump(encoders, f)
print("✓ encoders.pickle")

# Salvar scaler
with open('../models/scaler_cluster.pickle', 'wb') as f:
    pickle.dump(scaler_cluster, f)
print("✓ scaler_cluster.pickle")

print("\n✅ Todos os modelos foram salvos com sucesso!")
print(f"Acurácia do classificador: {rf_classifier.score(X_class, y_class):.4f}")
print(f"R² do regressor: {gb_regressor.score(X_reg, y_reg):.4f}")
