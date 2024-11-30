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

            # Obter a chave da API do Gemini do arquivo .env
            api_key = os.getenv('GEMINI_API_KEY')

            if not api_key:
                return Response(
                    {"error": "Chave da API não configurada corretamente."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            # Configurar a API do Gemini
            genai.configure(api_key=api_key)
            
            current_directory = os.getcwd()
            promptJson = os.path.join(current_directory, "quiz", "exemploPrompt.json")

            with open(promptJson, "r", encoding="utf-8") as arquivo:
                dadosJson = json.load(arquivo)
            jsonDocs = json.dumps(dadosJson, indent=4)

            # Construir o prompt
            prompt = f"""Gere cinco questões sobre {assunto} em {materia}.
            Gere como exercícios de escola, dê 4 alternativas para cada questão (a, b, c e d) e indique apenas uma correta.
            É MUITO IMPORTANTE que a resposta seja um JSON válido exatamente neste formato: {jsonDocs}"""
            

            # Gerar conteúdo usando a API
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            texto_questoes = response.text.replace('```json', '').replace('```', '').strip()

            try:
                # Tentar fazer o parse do JSON retornado
                questoes_json = json.loads(texto_questoes)
                
                # Retornar o JSON parseado
                return Response(
                    questoes_json,
                    status=status.HTTP_200_OK
                )
            except json.JSONDecodeError as je:
                return Response(
                    {"error": f"Erro ao decodificar JSON da resposta: {str(je)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        except Exception as e:
            return Response(
                {"error": f"Erro ao gerar questões: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )