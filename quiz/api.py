import os
import json
import google.generativeai as genai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Caminho do arquivo JSON de exemplo
current_directory = os.getcwd()
promptJson = os.path.join(current_directory, "quiz", "exemploPrompt.json")

# Carregar o exemplo de JSON para ser usado no prompt
with open(promptJson, "r", encoding="utf-8") as arquivo:
    dadosJson = json.load(arquivo)

jsonDocs = json.dumps(dadosJson, indent=4)  # Serializar o JSON para usá-lo no prompt

class GerarQuestaoAPIView(APIView):
    """
    API para gerar questões utilizando o modelo Gemini.
    Recebe parâmetros via POST (matéria e assunto) e retorna um JSON com as questões.
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
            genai.configure(api_key=os.getenv("AIzaSyDKilv1qBzn8ewXSziCaoWzUOM_aQWVVhU"))  # Certifique-se de configurar sua chave corretamente

            # Construir o prompt
            prompt = f"""Gere cinco questões sobre {assunto} em {materia}.
            Gere como exercícios de escola, dê 4 alternativas para cada questão (a, b, c e d) e indique apenas uma correta.
            Sua resposta deve ser APENAS um JSON Puro sem texto adicional, seguindo este formato:
            {jsonDocs}

            Certifique-se de que a resposta esteja no mesmo formato e seja válida."""

            # Gerar conteúdo usando a API
            response = genai.generate_content(prompt)

            # Limpar delimitadores de código, se presentes
            raw_response = response.result.strip("```json").strip("```").strip()

            # Tentar carregar a resposta como JSON
            questoes_json = json.loads(raw_response)

            # Retornar o JSON formatado para o cliente
            return Response(questoes_json, status=status.HTTP_200_OK)

        except json.JSONDecodeError as e:
            # Erro ao decodificar o JSON retornado pela Gemini
            return Response(
                {"error": f"Erro ao processar a resposta da Gemini: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            # Retornar erro genérico para outros casos
            return Response(
                {"error": f"Erro ao gerar questões: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
