from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Comando para testar configuração'

    def handle(self, *args, **kwargs):
        self.stdout.write("O comando testar_comando foi executado com sucesso!")
