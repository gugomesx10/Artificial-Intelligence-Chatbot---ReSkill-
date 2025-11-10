"""
API REST ReSkill+ - Flask
Endpoints para modelos de IA e Chatbot
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# ============================================
# CARREGAMENTO DOS MODELOS
# ============================================

MODELS_DIR = '../models'
DATA_DIR = '../data'

# Variáveis globais para modelos
classificador = None
regressor = None
clustering = None
encoders = None
scaler = None
df_cursos = None

def carregar_modelos():
    """Carrega todos os modelos e dados necessários"""
    global classificador, regressor, clustering, encoders, scaler, df_cursos
    
    try:
        # Carregar modelos
        with open(f'{MODELS_DIR}/classificador_perfil.pickle', 'rb') as f:
            classificador = pickle.load(f)
        
        with open(f'{MODELS_DIR}/regressor_risco.pickle', 'rb') as f:
            regressor = pickle.load(f)
        
        with open(f'{MODELS_DIR}/clustering_kmeans.pickle', 'rb') as f:
            clustering = pickle.load(f)
        
        with open(f'{MODELS_DIR}/encoders.pickle', 'rb') as f:
            encoders = pickle.load(f)
        
        with open(f'{MODELS_DIR}/scaler_cluster.pickle', 'rb') as f:
            scaler = pickle.load(f)
        
        # Carregar dataset de cursos
        df_cursos = pd.read_csv(f'{DATA_DIR}/cursos_recomendacao.csv')
        
        print("✅ Modelos carregados com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao carregar modelos: {str(e)}")
        return False

# ============================================
# ENDPOINTS DA API
# ============================================

@app.route('/')
def home():
    """Endpoint raiz com informações da API"""
    return jsonify({
        'nome': 'ReSkill+ API',
        'versao': '1.0.0',
        'descricao': 'API REST para modelos de IA e Chatbot do ReSkill+',
        'endpoints': {
            'GET /': 'Informações da API',
            'GET /health': 'Status de saúde da API',
            'POST /api/perfil/prever': 'Predição do perfil do trabalhador',
            'POST /api/risco/prever': 'Predição do risco de automação',
            'POST /api/cluster/segmentar': 'Segmentação de trabalhador',
            'POST /api/cursos/recomendar': 'Recomendação de cursos',
            'POST /api/chatbot/interagir': 'Interação com chatbot',
            'GET /api/cursos/listar': 'Listar todos os cursos',
            'GET /api/estatisticas': 'Estatísticas dos modelos'
        }
    })

@app.route('/health')
def health():
    """Verifica o status de saúde da API"""
    modelos_ok = all([
        classificador is not None,
        regressor is not None,
        clustering is not None,
        encoders is not None,
        scaler is not None,
        df_cursos is not None
    ])
    
    return jsonify({
        'status': 'healthy' if modelos_ok else 'unhealthy',
        'timestamp': datetime.now().isoformat(),
        'modelos_carregados': modelos_ok
    }), 200 if modelos_ok else 503

@app.route('/api/perfil/prever', methods=['POST'])
def prever_perfil():
    """
    Prediz o perfil do trabalhador
    
    Body JSON esperado:
    {
        "idade": 30,
        "escolaridade": "superior",
        "anos_experiencia": 5,
        "area_atuacao": "TI",
        "habilidades_digitais": 8,
        "renda_mensal": 5000,
        "setor_industria": "tecnologia"
    }
    """
    try:
        dados = request.json
        
        # Validar dados obrigatórios
        campos_obrigatorios = ['idade', 'escolaridade', 'anos_experiencia', 
                               'area_atuacao', 'habilidades_digitais', 
                               'renda_mensal', 'setor_industria']
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                return jsonify({'erro': f'Campo obrigatório ausente: {campo}'}), 400
        
        # Codificar variáveis categóricas
        try:
            escolaridade_enc = encoders['le_escolaridade'].transform([dados['escolaridade']])[0]
            area_enc = encoders['le_area'].transform([dados['area_atuacao']])[0]
            setor_enc = encoders['le_setor'].transform([dados['setor_industria']])[0]
        except ValueError as e:
            return jsonify({'erro': f'Valor inválido para variável categórica: {str(e)}'}), 400
        
        # Preparar features
        X = [[
            dados['idade'],
            escolaridade_enc,
            dados['anos_experiencia'],
            area_enc,
            dados['habilidades_digitais'],
            dados['renda_mensal'],
            setor_enc
        ]]
        
        # Predição
        perfil_pred = classificador.predict(X)[0]
        perfil_nome = encoders['le_perfil'].inverse_transform([perfil_pred])[0]
        
        # Probabilidades
        perfil_proba = classificador.predict_proba(X)[0]
        probabilidades = {
            classe: float(prob) 
            for classe, prob in zip(encoders['le_perfil'].classes_, perfil_proba)
        }
        
        return jsonify({
            'perfil': perfil_nome,
            'probabilidades': probabilidades,
            'confianca': float(max(perfil_proba)),
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/risco/prever', methods=['POST'])
def prever_risco():
    """
    Prediz o risco de automação
    
    Body JSON esperado:
    {
        "repetitividade": 7,
        "criatividade_requerida": 3,
        "interacao_humana": 4,
        "complexidade_tecnica": 3,
        "nivel_educacao": 3
    }
    """
    try:
        dados = request.json
        
        # Validar dados obrigatórios
        campos_obrigatorios = ['repetitividade', 'criatividade_requerida', 
                               'interacao_humana', 'complexidade_tecnica', 
                               'nivel_educacao']
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                return jsonify({'erro': f'Campo obrigatório ausente: {campo}'}), 400
        
        # Preparar features
        X = [[
            dados['repetitividade'],
            dados['criatividade_requerida'],
            dados['interacao_humana'],
            dados['complexidade_tecnica'],
            dados['nivel_educacao']
        ]]
        
        # Predição
        risco = regressor.predict(X)[0]
        
        # Classificar nível de risco
        if risco < 30:
            nivel = 'baixo'
            mensagem = 'Profissão com baixo risco de automação'
        elif risco < 70:
            nivel = 'médio'
            mensagem = 'Profissão com risco moderado de automação'
        else:
            nivel = 'alto'
            mensagem = 'Profissão com alto risco de automação'
        
        return jsonify({
            'risco_automacao': float(risco),
            'nivel': nivel,
            'mensagem': mensagem,
            'recomendacao': 'Busque qualificação em áreas com maior criatividade e interação humana' if risco > 50 else 'Continue desenvolvendo suas habilidades',
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/cluster/segmentar', methods=['POST'])
def segmentar():
    """
    Segmenta o trabalhador em clusters
    
    Body JSON esperado:
    {
        "idade": 30,
        "anos_experiencia": 5,
        "habilidades_digitais": 8,
        "renda_mensal": 5000,
        "risco_automacao": 25.5
    }
    """
    try:
        dados = request.json
        
        # Validar dados obrigatórios
        campos_obrigatorios = ['idade', 'anos_experiencia', 'habilidades_digitais', 
                               'renda_mensal', 'risco_automacao']
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                return jsonify({'erro': f'Campo obrigatório ausente: {campo}'}), 400
        
        # Preparar features
        X = [[
            dados['idade'],
            dados['anos_experiencia'],
            dados['habilidades_digitais'],
            dados['renda_mensal'],
            dados['risco_automacao']
        ]]
        
        # Normalizar
        X_scaled = scaler.transform(X)
        
        # Predição do cluster
        cluster = int(clustering.predict(X_scaled)[0])
        
        # Descrições dos clusters
        cluster_descricoes = {
            0: 'Profissionais Tradicionais: Baixa qualificação digital, risco alto de automação',
            1: 'Profissionais em Transição: Qualificação intermediária, risco moderado',
            2: 'Profissionais Digitais: Alta qualificação, baixo risco de automação',
            3: 'Profissionais Seniores: Alta experiência e renda, risco variável'
        }
        
        return jsonify({
            'cluster': cluster,
            'descricao': cluster_descricoes.get(cluster, 'Cluster não identificado'),
            'caracteristicas': {
                'idade': dados['idade'],
                'anos_experiencia': dados['anos_experiencia'],
                'habilidades_digitais': dados['habilidades_digitais'],
                'renda_mensal': dados['renda_mensal'],
                'risco_automacao': dados['risco_automacao']
            },
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/cursos/recomendar', methods=['POST'])
def recomendar_cursos():
    """
    Recomenda cursos baseado no perfil
    
    Body JSON esperado:
    {
        "perfil": "tech_avancado",
        "area_interesse": "ia_ml",
        "nivel_atual": "intermediario",
        "top_n": 5
    }
    """
    try:
        dados = request.json
        perfil = dados.get('perfil', 'digital_intermediario')
        area = dados.get('area_interesse', None)
        nivel = dados.get('nivel_atual', None)
        top_n = dados.get('top_n', 5)
        
        # Filtrar cursos
        cursos_filtrados = df_cursos.copy()
        
        if perfil:
            cursos_filtrados = cursos_filtrados[cursos_filtrados['perfil'] == perfil]
        
        if area:
            cursos_filtrados = cursos_filtrados[cursos_filtrados['area_interesse'] == area]
        
        if nivel:
            cursos_filtrados = cursos_filtrados[cursos_filtrados['nivel_atual'] == nivel]
        
        # Ordenar por score de relevância
        cursos_filtrados = cursos_filtrados.sort_values('score_relevancia', ascending=False).head(top_n)
        
        # Converter para lista de dicionários
        recomendacoes = cursos_filtrados.to_dict('records')
        
        return jsonify({
            'total_encontrados': len(recomendacoes),
            'cursos': recomendacoes,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/cursos/listar', methods=['GET'])
def listar_cursos():
    """Lista todos os cursos disponíveis"""
    try:
        # Parâmetros de filtro opcionais
        perfil = request.args.get('perfil')
        nivel = request.args.get('nivel')
        
        cursos = df_cursos.copy()
        
        if perfil:
            cursos = cursos[cursos['perfil'] == perfil]
        
        if nivel:
            cursos = cursos[cursos['nivel_atual'] == nivel]
        
        return jsonify({
            'total': len(cursos),
            'cursos': cursos.to_dict('records')
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/chatbot/interagir', methods=['POST'])
def chatbot_interagir():
    """
    Chatbot para orientação do usuário
    
    Body JSON esperado:
    {
        "mensagem": "Quero aprender sobre IA",
        "contexto": {
            "perfil": "tech_avancado",
            "nivel": "intermediario"
        }
    }
    """
    try:
        dados = request.json
        mensagem = dados.get('mensagem', '').lower()
        contexto = dados.get('contexto', {})
        
        # Lógica simples de chatbot baseada em palavras-chave
        resposta = ""
        cursos_sugeridos = []
        
        # Detecção de intenções
        if any(palavra in mensagem for palavra in ['oi', 'olá', 'hello', 'ola']):
            resposta = "Olá! Sou o assistente virtual do ReSkill+. Como posso ajudá-lo em sua jornada de requalificação?"
        
        elif any(palavra in mensagem for palavra in ['curso', 'aprender', 'estudar', 'qualificação']):
            perfil = contexto.get('perfil', 'digital_intermediario')
            
            # Detectar área de interesse
            if any(palavra in mensagem for palavra in ['ia', 'inteligência artificial', 'machine learning', 'ml']):
                cursos = df_cursos[(df_cursos['perfil'] == perfil) & 
                                  (df_cursos['area_interesse'].str.contains('ia|ml|dados', na=False))].head(3)
                resposta = f"Excelente escolha! IA é uma área em crescimento. Aqui estão alguns cursos recomendados para seu perfil ({perfil}):"
            
            elif any(palavra in mensagem for palavra in ['python', 'programação', 'desenvolvimento']):
                cursos = df_cursos[(df_cursos['perfil'] == perfil) & 
                                  (df_cursos['area_interesse'].str.contains('desenvolvimento|mobile|frontend|backend', na=False))].head(3)
                resposta = "Programação é uma habilidade essencial! Veja esses cursos:"
            
            elif any(palavra in mensagem for palavra in ['dados', 'data', 'analytics']):
                cursos = df_cursos[(df_cursos['perfil'] == perfil) & 
                                  (df_cursos['area_interesse'].str.contains('dados|analytics|bi', na=False))].head(3)
                resposta = "Análise de dados é muito valorizada! Confira essas opções:"
            
            else:
                cursos = df_cursos[df_cursos['perfil'] == perfil].head(3)
                resposta = f"Aqui estão alguns cursos populares para seu perfil ({perfil}):"
            
            cursos_sugeridos = cursos.to_dict('records') if not cursos.empty else []
        
        elif any(palavra in mensagem for palavra in ['risco', 'automação', 'substituído', 'substituir']):
            resposta = "A automação está transformando o mercado de trabalho. Para avaliar seu risco, posso analisar características da sua ocupação como repetitividade, criatividade e interação humana. Profissões que exigem criatividade e relacionamento interpessoal tendem a ter menor risco."
        
        elif any(palavra in mensagem for palavra in ['ajuda', 'help', 'como funciona']):
            resposta = """Posso ajudá-lo com:
            
            • Recomendação de cursos personalizados
            • Avaliação do risco de automação da sua profissão
            • Orientação sobre trilhas de aprendizado
            • Informações sobre áreas em crescimento
            
            O que você gostaria de saber?"""
        
        elif any(palavra in mensagem for palavra in ['obrigado', 'valeu', 'thanks']):
            resposta = "Por nada! Estou aqui para ajudar em sua jornada de requalificação. Boa sorte! 🚀"
        
        else:
            resposta = "Desculpe, não entendi bem. Posso ajudá-lo com recomendações de cursos, avaliação de risco de automação ou informações sobre trilhas de aprendizado. O que você precisa?"
        
        return jsonify({
            'resposta': resposta,
            'cursos_sugeridos': cursos_sugeridos,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/estatisticas', methods=['GET'])
def estatisticas():
    """Retorna estatísticas dos modelos e dados"""
    try:
        stats = {
            'total_cursos': len(df_cursos),
            'cursos_por_perfil': df_cursos['perfil'].value_counts().to_dict(),
            'cursos_por_nivel': df_cursos['nivel_atual'].value_counts().to_dict(),
            'modalidades': df_cursos['modalidade'].value_counts().to_dict(),
            'duracao_media': float(df_cursos['duracao_horas'].mean()),
            'custo_medio': float(df_cursos['custo'].mean()),
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(stats)
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ============================================
# INICIALIZAÇÃO
# ============================================

if __name__ == '__main__':
    print("="*60)
    print("Inicializando API ReSkill+...")
    print("="*60)
    
    # Carregar modelos
    if carregar_modelos():
        print("\n🚀 API pronta para uso!")
        print("📡 Acesse: http://localhost:5000")
        print("="*60)
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("\n❌ Erro ao inicializar API. Verifique os modelos.")
        print("Execute o notebook 'modelos_ia_reskill.ipynb' para gerar os modelos.")
