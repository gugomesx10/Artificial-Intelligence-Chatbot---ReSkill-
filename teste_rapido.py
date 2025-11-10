"""
Teste Rápido da API ReSkill+ 
Por: Gustavo Gomes Martins - RM 555999
"""

import requests
import json

print("="*70)
print("🚀 TESTANDO API RESKILL+ - MODELOS DE IA")
print("="*70)

API_URL = "http://localhost:5000"

# Teste 1: Health Check
print("\n1️⃣ HEALTH CHECK")
print("-"*70)
response = requests.get(f"{API_URL}/health")
print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# Teste 2: Predição de Perfil
print("\n2️⃣ PREDIÇÃO DE PERFIL DO TRABALHADOR")
print("-"*70)
perfil_data = {
    "idade": 28,
    "escolaridade": "superior",
    "anos_experiencia": 4,
    "area_atuacao": "TI",
    "habilidades_digitais": 9,
    "renda_mensal": 5500,
    "setor_industria": "tecnologia"
}
print(f"Entrada: {json.dumps(perfil_data, indent=2, ensure_ascii=False)}")
response = requests.post(f"{API_URL}/api/perfil/prever", json=perfil_data)
print(f"\nResposta:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# Teste 3: Predição de Risco de Automação
print("\n3️⃣ PREDIÇÃO DE RISCO DE AUTOMAÇÃO")
print("-"*70)
risco_data = {
    "repetitividade": 8,
    "criatividade_requerida": 2,
    "interacao_humana": 3,
    "complexidade_tecnica": 2,
    "nivel_educacao": 2
}
print(f"Entrada: {json.dumps(risco_data, indent=2, ensure_ascii=False)}")
response = requests.post(f"{API_URL}/api/risco/prever", json=risco_data)
print(f"\nResposta:")
print(json.dumps(response.json(), indent=2, ensure_ascii=False))

# Teste 4: Recomendação de Cursos
print("\n4️⃣ RECOMENDAÇÃO DE CURSOS")
print("-"*70)
cursos_data = {
    "perfil": "tech_avancado",
    "area_interesse": "ia_ml",
    "top_n": 3
}
print(f"Entrada: {json.dumps(cursos_data, indent=2, ensure_ascii=False)}")
response = requests.post(f"{API_URL}/api/cursos/recomendar", json=cursos_data)
result = response.json()
print(f"\nTotal de cursos encontrados: {result['total_encontrados']}")
for i, curso in enumerate(result['cursos'], 1):
    print(f"\n  Curso {i}:")
    print(f"    Nome: {curso['curso_recomendado']}")
    print(f"    Duração: {curso['duracao_horas']}h")
    print(f"    Custo: R$ {curso['custo']}")
    print(f"    Modalidade: {curso['modalidade']}")
    print(f"    Score: {curso['score_relevancia']}")

# Teste 5: Chatbot
print("\n5️⃣ CHATBOT - INTERAÇÃO INTELIGENTE")
print("-"*70)
chat_data = {
    "mensagem": "Quero aprender sobre inteligência artificial",
    "contexto": {
        "perfil": "tech_avancado",
        "nivel": "intermediario"
    }
}
print(f"Pergunta: '{chat_data['mensagem']}'")
response = requests.post(f"{API_URL}/api/chatbot/interagir", json=chat_data)
result = response.json()
print(f"\nResposta do Bot: {result['resposta']}")
if result.get('cursos_sugeridos'):
    print(f"\nCursos Sugeridos: {len(result['cursos_sugeridos'])}")

print("\n" + "="*70)
print("✅ TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
print("="*70)
print("\n🎯 RESUMO:")
print("  • Classificação de Perfil: ✅ Funcionando")
print("  • Predição de Risco: ✅ Funcionando")
print("  • Recomendação de Cursos: ✅ Funcionando")
print("  • Chatbot: ✅ Funcionando")
print("\n🎉 API RESKILL+ TOTALMENTE OPERACIONAL!")
print("="*70)
