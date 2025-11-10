"""
Script de teste para a API ReSkill+
Execute este script para testar todos os endpoints da API
"""

import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000"

def print_response(title, response):
    """Imprime a resposta de forma formatada"""
    print(f"\n{'='*60}")
    print(f"🔹 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

def test_api():
    """Testa todos os endpoints da API"""
    
    print("🚀 Iniciando testes da API ReSkill+")
    print(f"URL Base: {BASE_URL}")
    
    # 1. Teste de informações da API
    print_response(
        "GET / - Informações da API",
        requests.get(f"{BASE_URL}/")
    )
    
    # 2. Teste de health check
    print_response(
        "GET /health - Health Check",
        requests.get(f"{BASE_URL}/health")
    )
    
    # 3. Teste de predição de perfil
    perfil_data = {
        "idade": 28,
        "escolaridade": "superior",
        "anos_experiencia": 4,
        "area_atuacao": "TI",
        "habilidades_digitais": 9,
        "renda_mensal": 5500,
        "setor_industria": "tecnologia"
    }
    print_response(
        "POST /api/perfil/prever - Predição de Perfil",
        requests.post(f"{BASE_URL}/api/perfil/prever", json=perfil_data)
    )
    
    # 4. Teste de predição de risco
    risco_data = {
        "repetitividade": 8,
        "criatividade_requerida": 2,
        "interacao_humana": 3,
        "complexidade_tecnica": 2,
        "nivel_educacao": 2
    }
    print_response(
        "POST /api/risco/prever - Predição de Risco",
        requests.post(f"{BASE_URL}/api/risco/prever", json=risco_data)
    )
    
    # 5. Teste de segmentação
    cluster_data = {
        "idade": 30,
        "anos_experiencia": 5,
        "habilidades_digitais": 8,
        "renda_mensal": 5000,
        "risco_automacao": 25.5
    }
    print_response(
        "POST /api/cluster/segmentar - Segmentação",
        requests.post(f"{BASE_URL}/api/cluster/segmentar", json=cluster_data)
    )
    
    # 6. Teste de recomendação de cursos
    cursos_data = {
        "perfil": "tech_avancado",
        "area_interesse": "ia_ml",
        "nivel_atual": "intermediario",
        "top_n": 3
    }
    print_response(
        "POST /api/cursos/recomendar - Recomendação de Cursos",
        requests.post(f"{BASE_URL}/api/cursos/recomendar", json=cursos_data)
    )
    
    # 7. Teste de listagem de cursos
    print_response(
        "GET /api/cursos/listar - Listar Cursos",
        requests.get(f"{BASE_URL}/api/cursos/listar?perfil=tech_avancado")
    )
    
    # 8. Teste de chatbot
    chat_data = {
        "mensagem": "Quero aprender sobre machine learning",
        "contexto": {
            "perfil": "digital_intermediario",
            "nivel": "intermediario"
        }
    }
    print_response(
        "POST /api/chatbot/interagir - Chatbot",
        requests.post(f"{BASE_URL}/api/chatbot/interagir", json=chat_data)
    )
    
    # 9. Teste de estatísticas
    print_response(
        "GET /api/estatisticas - Estatísticas",
        requests.get(f"{BASE_URL}/api/estatisticas")
    )
    
    print("\n" + "="*60)
    print("✅ Testes concluídos!")
    print("="*60)

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ Erro: Não foi possível conectar à API.")
        print("Certifique-se de que a API está rodando em http://localhost:5000")
        print("\nPara iniciar a API, execute:")
        print("  cd api")
        print("  python app.py")
    except Exception as e:
        print(f"\n❌ Erro ao executar testes: {str(e)}")
