import os
import requests
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Caminho construído a partir do diretório atual
current_directory = os.getcwd()
promptJson = os.path.join(current_directory, "quiz", "exemploPrompt.json")

with open(promptJson, "r", encoding="utf-8") as arquivo:
    dadosJson = json.load(arquivo)

jsonDocs = json.dumps(dadosJson, indent=4)

def gerar_questao(area, materia, assunto):
    """Gera uma questão utilizando a API do Gemini.

    Args:
        area (str): Área do conhecimento.
        materia (str): Matéria específica.
        assunto (str): Assunto da questão.

    Returns:
        dict: Dicionário contendo a resposta da API ou informações sobre o erro.
    """
    try:
        # Configure the API key
        genai.configure(api_key="AIzaSyAA4jvpnCviU9iX8fLlu9YIK4XKN8PS08M")

        # Use triple quotes for a multiline string
        prompt = f"""Gere uma questão sobre {assunto} em {materia}, na área de {area}. 
        Gere como um Exercício de escola, dê 4 alternativas a, b, c e d (somente uma correta). 
        Isso é um prompt para uma aplicação, me dê como resposta APENAS um json, como no seguinte exemplo: {jsonDocs}"""

        # Create the model and generate content
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        print(response.text)

    except Exception as e:
        print(f"Algum erro ocorreu: {e}")

# Teste a função
gerar_questao("Subtração", "Matematica", "Algebra")
