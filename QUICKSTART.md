# 🚀 Guia Rápido de Início - ReSkill+

## Passo a Passo para Executar o Projeto

### 1. Instalar Dependências

```bash
# Navegar até a pasta do projeto
cd "Artificial-Intelligence-Chatbot---ReSkill-"

# Instalar bibliotecas necessárias
pip install flask flask-cors pandas numpy scikit-learn matplotlib seaborn jupyter
```

### 2. Treinar os Modelos

**Opção A - Usando Jupyter Notebook (Recomendado)**:

```bash
# Instalar Jupyter
pip install jupyter

# Abrir o notebook
jupyter notebook notebooks/modelos_ia_reskill.ipynb
```

Execute todas as células do notebook (Cell > Run All)

**Opção B - Usando script Python**:

```bash
cd notebooks
python gerar_modelos.py
```

Isso criará os arquivos na pasta `models/`:
- ✅ classificador_perfil.pickle
- ✅ regressor_risco.pickle
- ✅ clustering_kmeans.pickle
- ✅ encoders.pickle
- ✅ scaler_cluster.pickle

### 3. Executar a API

```bash
# Voltar para a raiz e ir para a pasta api
cd api

# Executar a API
python app.py
```

Você verá:
```
Inicializando API ReSkill+...
✅ Modelos carregados com sucesso!
🚀 API pronta para uso!
📡 Acesse: http://localhost:5000
```

### 4. Testar a API

**No navegador**:
- Acesse http://localhost:5000

**Usando o script de teste**:
```bash
# Em outro terminal
cd api
python test_api.py
```

**Usando cURL**:
```bash
curl http://localhost:5000/health
```

**Usando Python**:
```python
import requests

# Testar health check
response = requests.get("http://localhost:5000/health")
print(response.json())

# Predição de perfil
data = {
    "idade": 28,
    "escolaridade": "superior",
    "anos_experiencia": 4,
    "area_atuacao": "TI",
    "habilidades_digitais": 9,
    "renda_mensal": 5500,
    "setor_industria": "tecnologia"
}
response = requests.post("http://localhost:5000/api/perfil/prever", json=data)
print(response.json())
```

---

## 📊 Estrutura de Pastas

```
Artificial-Intelligence-Chatbot---ReSkill-/
│
├── 📁 data/                    # Datasets CSV
├── 📁 notebooks/               # Jupyter Notebooks
├── 📁 models/                  # Modelos treinados (.pickle)
├── 📁 api/                     # API Flask
│   ├── app.py                 # Código da API
│   ├── requirements.txt       # Dependências
│   └── test_api.py            # Script de teste
├── GRUPO.txt                   # Info do grupo
├── README.md                   # Documentação
└── QUICKSTART.md              # Este arquivo
```

---

## 🔧 Solução de Problemas

### Erro: "ModuleNotFoundError"
```bash
# Instale a biblioteca faltante
pip install nome_da_biblioteca
```

### Erro: "Modelos não encontrados"
```bash
# Execute o notebook ou script para gerar os modelos
cd notebooks
python gerar_modelos.py
```

### API não inicia
- Verifique se a porta 5000 está livre
- Certifique-se de que os modelos foram gerados
- Verifique se todas as dependências estão instaladas

### Erro ao carregar dados
- Verifique se os arquivos CSV estão na pasta `data/`
- Certifique-se de que os caminhos relativos estão corretos

---

## 📝 Endpoints Principais

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Informações da API |
| GET | `/health` | Status de saúde |
| POST | `/api/perfil/prever` | Predição de perfil |
| POST | `/api/risco/prever` | Risco de automação |
| POST | `/api/cursos/recomendar` | Recomendação de cursos |
| POST | `/api/chatbot/interagir` | Interação com chatbot |

---

## 💡 Dicas

1. **Use o notebook primeiro**: Execute `modelos_ia_reskill.ipynb` para entender o pipeline completo
2. **Teste gradualmente**: Teste um endpoint de cada vez
3. **Veja os logs**: A API mostra logs úteis no terminal
4. **Use o test_api.py**: Script automático para testar todos os endpoints
5. **Consulte o README.md**: Documentação completa com exemplos

---

## ✅ Checklist de Entrega

- [ ] 3 datasets CSV na pasta `data/`
- [ ] Notebook completo em `notebooks/`
- [ ] 5 arquivos .pickle na pasta `models/`
- [ ] API funcionando em `api/app.py`
- [ ] Arquivo `GRUPO.txt` com informações do grupo
- [ ] README.md atualizado

---

## 🎯 Pontuação

- ✅ Dados (CSV): 10 pontos
- ✅ Notebooks: 60 pontos
- ✅ Modelos (.pickle): 10 pontos
- ✅ API REST (.py): 20 pontos
- ✅ Grupo (.txt): Documentação

**Total: 100 pontos**

---

**Boa sorte! 🚀**
