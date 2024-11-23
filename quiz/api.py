import os
import json
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class GerarQuestaoAPIView(APIView):
    """
    API para gerar questões utilizando o modelo Gemini.
    Recebe parâmetros via POST (matéria e assunto) e retorna o texto das questões.
    """
    def post(self, request):
        try:
            # Extrair parâmetros do corpo da requisição
            materia = request.data.get('materia')
            assunto = request.data.get('assunto')

            # Verificar se os parâmetros obrigatórios foram enviados
            if not materia or not assunto:
                return Response(
                    {"error": "Os campos 'materia' e 'assunto' são obrigatórios."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Configurar a API do Gemini
            genai.configure(api_key="AIzaSyDKilv1qBzn8ewXSziCaoWzUOM_aQWVVhU")

            
            current_directory = os.getcwd()
            promptJson = os.path.join(current_directory, "quiz", "exemploPrompt.json")

            with open(promptJson, "r", encoding="utf-8") as arquivo:
                dadosJson = json.load(arquivo)
            jsonDocs = json.dumps(dadosJson, indent=4)

            # Construir o prompt
            prompt = f"""Gere cinco questões sobre {assunto} em {materia}.
            Gere como exercícios de escola, dê 4 alternativas para cada questão (a, b, c e d) e indique apenas uma correta.
            Formate a sua resposta desse jeito: {jsonDocs}"""
            

            # Gerar conteúdo usando a API
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            texto_questoes = response.text.replace('**', '')

            #print(texto_questoes)

            # Obter o texto da resposta
            texto_questoes = response.text.replace('\n', ' ').strip()

            texto_questoes = ' '.join(texto_questoes.split())

            #print(texto_questoes)

            # Retornar o texto formatado para o cliente
            return Response(
                {"questoes": texto_questoes},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            # Retornar erro genérico para outros casos
            return Response(
                {"error": f"Erro ao gerar questões: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )