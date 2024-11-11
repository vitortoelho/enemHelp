import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def gerar_questao(area, materia, assunto):
    """Gera uma questão utilizando a API do Gemini.

    Args:
        area (str): Área do conhecimento.
        materia: (str): Matéria específica.
        assunto: (str): Assunto da questão.

    Returns:
        dict: Dicionário contendo a resposta da API ou informações sobre o erro.
    """

    chave_api = os.getenv("GEMINI_API_KEY")
    if not chave_api:
        return {"error": "Chave da API não encontrada. Verifique o arquivo .env."}

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyDKilv1qBzn8ewXSziCaoWzUOM_aQWVVhU"
    headers = {}

    # **Adapte o payload de acordo com a documentação da API**
    payload = {
        "prompt": f"Gere uma questão sobre {assunto} em {materia}, na área de {area}.",
        "temperature": 0.7  # Ajuste a temperatura para controlar a criatividade da resposta
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Lança uma exceção para status codes diferentes de 200

        # Extrair a resposta da API
        resposta_ia = response.json()
        # Processar a resposta da IA (extrair a questão e as alternativas)
        # ...

        return resposta_ia
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao conectar com a API: {e}"}
    except json.JSONDecodeError as e:
        return {"error": f"Erro ao processar a resposta JSON: {e}"}