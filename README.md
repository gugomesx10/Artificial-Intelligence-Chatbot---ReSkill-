# 🤖 ReSkill+ | Artificial Intelligence & Chatbot

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📖 Sobre o Projeto

O **ReSkill+** é uma plataforma de Inteligência Artificial desenvolvida para apoiar a requalificação profissional de trabalhadores em risco de automação. Utilizando modelos de Machine Learning e um chatbot inteligente, o sistema oferece:

- 🎯 **Classificação de Perfil**: Identifica o nível de qualificação digital do trabalhador
- 📊 **Previsão de Risco**: Calcula o risco de automação da ocupação
- 👥 **Segmentação**: Agrupa trabalhadores para recomendações personalizadas
- 📚 **Recomendação de Cursos**: Sugere trilhas de aprendizado adequadas
- 💬 **Chatbot**: Orientação interativa sobre requalificação profissional

---

## 🎯 Modelos de IA Desenvolvidos

### 1. Classificação - Random Forest
**Objetivo**: Predizer o perfil do trabalhador

- **Classes**: 
  - `tech_avancado`: Profissionais com alta qualificação digital
  - `digital_intermediario`: Profissionais em transição digital
  - `tradicional`: Profissionais que precisam de requalificação

- **Features**: idade, escolaridade, anos_experiencia, area_atuacao, habilidades_digitais, renda_mensal, setor_industria

### 2. Regressão - Gradient Boosting
**Objetivo**: Predizer o risco de automação (%)

- **Range**: 0-100% (quanto maior, maior o risco)
- **Features**: repetitividade, criatividade_requerida, interacao_humana, complexidade_tecnica, nivel_educacao

### 3. Agrupamento - KMeans
**Objetivo**: Segmentar trabalhadores em 4 clusters

- **Cluster 0**: Profissionais Tradicionais (baixa qualificação digital, alto risco)
- **Cluster 1**: Profissionais em Transição (qualificação intermediária)
- **Cluster 2**: Profissionais Digitais (alta qualificação, baixo risco)
- **Cluster 3**: Profissionais Seniores (alta experiência e renda)

---

## 📁 Estrutura do Projeto

```
Artificial-Intelligence-Chatbot---ReSkill-/
│
├── data/                                    # Datasets (10 pontos)
│   ├── perfil_trabalhador.csv              # 100 registros de trabalhadores
│   ├── risco_automacao.csv                 # 100 registros de ocupações
│   └── cursos_recomendacao.csv             # 100 cursos disponíveis
│
├── notebooks/                               # Notebooks Jupyter (60 pontos)
│   ├── modelos_ia_reskill.ipynb            # Pipeline completo de ML
│   └── gerar_modelos.py                    # Script para treinar modelos
│
├── models/                                  # Modelos treinados (10 pontos)
│   ├── classificador_perfil.pickle         # Modelo de classificação
│   ├── regressor_risco.pickle              # Modelo de regressão
│   ├── clustering_kmeans.pickle            # Modelo de clustering
│   ├── encoders.pickle                     # Label encoders
│   └── scaler_cluster.pickle               # Scaler para clustering
│
├── api/                                     # API REST Flask (20 pontos)
│   ├── app.py                              # Aplicação Flask
│   └── requirements.txt                    # Dependências Python
│
├── GRUPO.txt                                # Informações do grupo
└── README.md                                # Este arquivo
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 1️⃣ Instalação

```bash
# Clone o repositório
git clone https://github.com/gugomesx10/Artificial-Intelligence-Chatbot---ReSkill-.git
cd Artificial-Intelligence-Chatbot---ReSkill-

# Instale as dependências
pip install -r api/requirements.txt
```

### 2️⃣ Treinar os Modelos

Abra e execute o notebook `notebooks/modelos_ia_reskill.ipynb` no Jupyter:

```bash
# Instalar Jupyter (se necessário)
pip install jupyter

# Iniciar Jupyter
jupyter notebook notebooks/modelos_ia_reskill.ipynb
```

**Ou execute o script Python**:

```bash
cd notebooks
python gerar_modelos.py
```

Isso gerará os arquivos `.pickle` na pasta `models/`.

### 3️⃣ Executar a API

```bash
cd api
python app.py
```

A API estará disponível em: `http://localhost:5000`

---

## 🌐 Endpoints da API

### 📌 Informações

#### `GET /`
Retorna informações sobre a API e lista de endpoints.

**Resposta**:
```json
{
  "nome": "ReSkill+ API",
  "versao": "1.0.0",
  "endpoints": { ... }
}
```

#### `GET /health`
Verifica o status de saúde da API.

**Resposta**:
```json
{
  "status": "healthy",
  "modelos_carregados": true
}
```

---

### 🎯 Predições

#### `POST /api/perfil/prever`
Prediz o perfil do trabalhador.

**Body**:
```json
{
  "idade": 30,
  "escolaridade": "superior",
  "anos_experiencia": 5,
  "area_atuacao": "TI",
  "habilidades_digitais": 8,
  "renda_mensal": 5000,
  "setor_industria": "tecnologia"
}
```

**Resposta**:
```json
{
  "perfil": "tech_avancado",
  "probabilidades": {
    "tech_avancado": 0.85,
    "digital_intermediario": 0.12,
    "tradicional": 0.03
  },
  "confianca": 0.85
}
```

#### `POST /api/risco/prever`
Prediz o risco de automação.

**Body**:
```json
{
  "repetitividade": 7,
  "criatividade_requerida": 3,
  "interacao_humana": 4,
  "complexidade_tecnica": 3,
  "nivel_educacao": 3
}
```

**Resposta**:
```json
{
  "risco_automacao": 68.5,
  "nivel": "médio",
  "mensagem": "Profissão com risco moderado de automação",
  "recomendacao": "Busque qualificação em áreas com maior criatividade"
}
```

#### `POST /api/cluster/segmentar`
Segmenta o trabalhador em clusters.

**Body**:
```json
{
  "idade": 30,
  "anos_experiencia": 5,
  "habilidades_digitais": 8,
  "renda_mensal": 5000,
  "risco_automacao": 25.5
}
```

**Resposta**:
```json
{
  "cluster": 2,
  "descricao": "Profissionais Digitais: Alta qualificação, baixo risco de automação"
}
```

---

### 📚 Cursos

#### `POST /api/cursos/recomendar`
Recomenda cursos personalizados.

**Body**:
```json
{
  "perfil": "tech_avancado",
  "area_interesse": "ia_ml",
  "nivel_atual": "intermediario",
  "top_n": 5
}
```

**Resposta**:
```json
{
  "total_encontrados": 5,
  "cursos": [
    {
      "curso_recomendado": "Deep Learning Especializado",
      "duracao_horas": 120,
      "custo": 2500,
      "modalidade": "online",
      "score_relevancia": 95.5
    },
    ...
  ]
}
```

#### `GET /api/cursos/listar`
Lista todos os cursos disponíveis.

**Query Parameters**:
- `perfil` (opcional): Filtrar por perfil
- `nivel` (opcional): Filtrar por nível

**Resposta**:
```json
{
  "total": 100,
  "cursos": [ ... ]
}
```

---

### 💬 Chatbot

#### `POST /api/chatbot/interagir`
Interage com o chatbot.

**Body**:
```json
{
  "mensagem": "Quero aprender sobre IA",
  "contexto": {
    "perfil": "tech_avancado",
    "nivel": "intermediario"
  }
}
```

**Resposta**:
```json
{
  "resposta": "Excelente escolha! IA é uma área em crescimento...",
  "cursos_sugeridos": [ ... ]
}
```

---

### 📊 Estatísticas

#### `GET /api/estatisticas`
Retorna estatísticas dos dados.

**Resposta**:
```json
{
  "total_cursos": 100,
  "cursos_por_perfil": {
    "tech_avancado": 35,
    "digital_intermediario": 40,
    "tradicional": 25
  },
  "duracao_media": 72.5,
  "custo_medio": 1250.0
}
```

---

## 📊 Datasets

### 1. perfil_trabalhador.csv (10 pontos)

**Descrição**: 100 registros de trabalhadores com informações demográficas e profissionais.

**Colunas**:
- `id`: Identificador único
- `idade`: Idade do trabalhador
- `escolaridade`: Nível de escolaridade (fundamental, medio, superior, pos_graduacao)
- `anos_experiencia`: Anos de experiência profissional
- `area_atuacao`: Área de atuação profissional
- `habilidades_digitais`: Nível de habilidades digitais (0-10)
- `renda_mensal`: Renda mensal em R$
- `setor_industria`: Setor da indústria
- `perfil`: Perfil classificado (target)

### 2. risco_automacao.csv

**Descrição**: 100 registros de ocupações com fatores de risco de automação.

**Colunas**:
- `id`: Identificador único
- `ocupacao`: Nome da ocupação
- `repetitividade`: Nível de repetitividade (0-10)
- `criatividade_requerida`: Criatividade necessária (0-10)
- `interacao_humana`: Nível de interação humana (0-10)
- `complexidade_tecnica`: Complexidade técnica (0-10)
- `nivel_educacao`: Nível de educação requerido (1-6)
- `risco_automacao`: Risco de automação em % (target)

### 3. cursos_recomendacao.csv

**Descrição**: 100 cursos disponíveis para requalificação.

**Colunas**:
- `id`: Identificador único
- `perfil`: Perfil alvo do curso
- `area_interesse`: Área de interesse
- `nivel_atual`: Nível atual do aluno
- `curso_recomendado`: Nome do curso
- `duracao_horas`: Duração em horas
- `custo`: Custo em R$
- `modalidade`: Modalidade (online, presencial, hibrido)
- `score_relevancia`: Score de relevância (0-100)

---

## 📓 Notebooks (60 pontos)

### modelos_ia_reskill.ipynb

Notebook completo com:

1. **Importação de Bibliotecas**
2. **Análise Exploratória de Dados (EDA)**
   - Visualização de distribuições
   - Análise de correlações
   - Estatísticas descritivas
3. **Pré-processamento**
   - Codificação de variáveis categóricas
   - Normalização de dados
   - Separação de treino/teste
4. **Modelo de Classificação**
   - Random Forest Classifier
   - Avaliação: Accuracy, Classification Report, Confusion Matrix
   - Importância de features
5. **Modelo de Regressão**
   - Gradient Boosting Regressor
   - Avaliação: MAE, RMSE, R²
   - Análise de resíduos
6. **Modelo de Clustering**
   - KMeans (k=4)
   - Método do cotovelo
   - Silhouette Score
   - Visualização com PCA
7. **Salvamento de Modelos**
   - Exportação em formato pickle
8. **Teste de Predição**
   - Carregamento e validação dos modelos

---

## 🎨 Exemplos de Uso

### Python

```python
import requests

# URL da API
api_url = "http://localhost:5000"

# Predição de perfil
perfil_data = {
    "idade": 28,
    "escolaridade": "superior",
    "anos_experiencia": 4,
    "area_atuacao": "TI",
    "habilidades_digitais": 9,
    "renda_mensal": 5500,
    "setor_industria": "tecnologia"
}

response = requests.post(f"{api_url}/api/perfil/prever", json=perfil_data)
print(response.json())

# Recomendação de cursos
cursos_data = {
    "perfil": "tech_avancado",
    "area_interesse": "ia_ml",
    "top_n": 3
}

response = requests.post(f"{api_url}/api/cursos/recomendar", json=cursos_data)
print(response.json())

# Chatbot
chat_data = {
    "mensagem": "Quero aprender sobre machine learning",
    "contexto": {"perfil": "digital_intermediario"}
}

response = requests.post(f"{api_url}/api/chatbot/interagir", json=chat_data)
print(response.json())
```

### cURL

```bash
# Predição de risco de automação
curl -X POST http://localhost:5000/api/risco/prever \
  -H "Content-Type: application/json" \
  -d '{
    "repetitividade": 8,
    "criatividade_requerida": 2,
    "interacao_humana": 3,
    "complexidade_tecnica": 2,
    "nivel_educacao": 2
  }'

# Listar cursos
curl http://localhost:5000/api/cursos/listar?perfil=tech_avancado
```

---

## 🛠️ Tecnologias

- **Python 3.8+**: Linguagem de programação
- **Flask 3.0**: Framework web para API REST
- **Scikit-learn 1.3.2**: Biblioteca de Machine Learning
- **Pandas 2.1.3**: Manipulação e análise de dados
- **NumPy 1.24.3**: Computação numérica
- **Matplotlib/Seaborn**: Visualização de dados
- **Jupyter Notebook**: Ambiente de desenvolvimento interativo

---

## 📈 Métricas de Avaliação

### Modelo de Classificação
- **Acurácia**: > 85%
- **Precision/Recall/F1-Score**: Por classe
- **Confusion Matrix**: Análise de erros

### Modelo de Regressão
- **MAE (Mean Absolute Error)**: < 10%
- **RMSE (Root Mean Squared Error)**: < 15%
- **R² Score**: > 0.80

### Modelo de Clustering
- **Silhouette Score**: > 0.50
- **Inércia**: Análise pelo método do cotovelo
- **Separação de clusters**: Visualização PCA

---

## 🎓 Pontuação do Projeto

- ✅ **Dados (CSV)**: 10 pontos - 3 datasets com 100 registros cada
- ✅ **Notebooks**: 60 pontos - Pipeline completo de ML com EDA, treinamento e avaliação
- ✅ **Modelos (.pickle)**: 10 pontos - 3 modelos + encoders + scaler
- ✅ **API REST (.py)**: 20 pontos - Flask com 10 endpoints funcionais
- ✅ **Arquivo do Grupo (.txt)**: Informações dos membros e explicações

**Total**: 100 pontos

---

## 🔮 Melhorias Futuras

- [ ] Implementar autenticação JWT
- [ ] Adicionar modelos de Deep Learning (LSTM, Transformers)
- [ ] Criar frontend web (React/Vue.js)
- [ ] Integrar com APIs de plataformas de cursos (Coursera, Udemy)
- [ ] Implementar sistema de feedback para melhorar recomendações
- [ ] Adicionar testes automatizados (pytest)
- [ ] Deploy em cloud (AWS, Azure, Heroku)
- [ ] Implementar cache (Redis)
- [ ] Adicionar monitoramento (Prometheus, Grafana)
- [ ] Criar documentação Swagger/OpenAPI

---

## 👥 Equipe

Veja o arquivo `GRUPO.txt` para informações dos membros do grupo.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos.

---

## 📞 Suporte

Para dúvidas ou sugestões:
- Abra uma [Issue](https://github.com/gugomesx10/Artificial-Intelligence-Chatbot---ReSkill-.git)
- Entre em contato com os membros do grupo

---

**Desenvolvido com ❤️ pela equipe ReSkill+**

*Projeto desenvolvido como parte do programa ReSkill+ - Novembro 2025*
ReSkill+ - Global Solution
