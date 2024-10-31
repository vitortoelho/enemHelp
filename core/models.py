from django.db import models

class Area(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

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
