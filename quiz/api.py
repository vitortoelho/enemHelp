import os
import requests
import json
import google.generativeai as genai
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

    # **Adapte o payload de acordo com a documentação da API**
    try:
        genai.configure(api_key="AIzaSyAA4jvpnCviU9iX8fLlu9YIK4XKN8PS08M")
        prompt = f"Gere uma questão sobre {assunto} em {materia}, na área de {area}. Gere como um Exercício de escola, dê 4 alternativas a, b, c e d (somente uma correta)."
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        print(response.text)

    except:
        print("Algum erro ocorreu!")

    
# exemplo de codigo da doc que funciona    
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Write a story about a magic backpack.")
# print(response.text)

gerar_questao("Subtração","Matematica", "Algebra")
