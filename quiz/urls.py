from django.urls import path
from .api import GerarQuestaoAPIView

urlpatterns = [
    path('gerar-questao/', GerarQuestaoAPIView.as_view(), name='gerar_questao'),
]
