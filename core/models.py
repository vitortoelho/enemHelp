from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Area(models.Model):
    nome = models.CharField(max_length=100)

    def str(self):
        return self.nome

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'áreas'

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='materias')

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='assuntos')


    def __str__(self):
        return self.nome

class Questoes(models.Model):
    nome = models.CharField(max_length=100)
    enunciado = models.TextField()
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE, related_name='questões')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='questões')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='questões')

    DIFF = [
        ('mFacil', 'Muito fácil'), 
        ('facil', 'Fácil'),
        ('medio', 'Médio'),
        ('dificil', 'Difícil'),
        ('mDificil', 'Muito difícil')
    ]
    
    dificuldade = models.CharField(
        max_length=15,
        choices=DIFF,
        default='Medio' 
    )
    
    def __str__(self):
        return self.nome

class Alternativa(models.Model):
    texto = models.CharField(max_length=100)
    questoes = models.ForeignKey(Questoes, on_delete=models.CASCADE, related_name='alternativa')
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto
    
class Resultado(models.Model):
    questao = models.ForeignKey(Questoes, on_delete=models.CASCADE, null=True, related_name='resultados')
    alternativa = models.ForeignKey(Alternativa, on_delete=models.CASCADE, null=True, related_name='resultados')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='resultados')
    acerto = models.BooleanField(default=False)

    def __str__(self):
        return f"Resultado do usuário {self.usuario.username} para a questão {self.questao.nome}"