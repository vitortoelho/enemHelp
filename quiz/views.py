from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def gerar_questao(dificuldade, assunto):
    # Função que gera a questão com base nos parâmetros fornecidos
    return {
        "dificuldade": dificuldade,
        "assunto": assunto,
        "questao": f"Questão gerada sobre {assunto} com dificuldade {dificuldade}."
    }

class GerarQuestaoAPIView(APIView):
    """
    API para gerar uma questão baseada nos parâmetros enviados via POST.
    """
    def post(self, request):
        try:
            # Lê os dados do corpo da requisição
            dificuldade = request.data.get('dificuldade')
            assunto = request.data.get('assunto')

            # Verifica se os parâmetros necessários estão presentes
            if not dificuldade or not assunto:
                return Response(
                    {"error": "Os campos 'dificuldade' e 'assunto' são obrigatórios."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Chama a função para gerar a questão
            questao = gerar_questao(dificuldade, assunto)
            return Response(questao, status=status.HTTP_200_OK)

        except Exception as e:
            # Retorna erro caso algo inesperado aconteça
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
