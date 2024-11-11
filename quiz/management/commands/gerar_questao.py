from django.core.management.base import BaseCommand
from quiz.api import gerar_questao  # Certifique-se de que api.py tem a função gerar_questao
import os


class Command(BaseCommand):
    help = 'Gera questões a partir da API Gemini Flash'

    def handle(self, *args, **kwargs):
        area = "Matemática"
        materia = "Álgebra"
        assunto = "Equações"

        # Executa a função gerar_questao sem passar a chave explícita
        result = gerar_questao(area, materia, assunto)

        if 'error' in result:
            self.stdout.write(self.style.ERROR(f"Erro: {result['error']}"))
        else:
            self.stdout.write(self.style.SUCCESS("Questões geradas com sucesso!"))
            self.stdout.write(str(result))
