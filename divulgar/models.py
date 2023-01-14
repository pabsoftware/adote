from django.db import models
from django.contrib.auth. models import User

# Create your models here.

class Raca(models.Model):
    raca = models.CharField(max_length=80)

    def __str__(self):
        return self.raca


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag
    
class Pet(models.Model):
    choices_status = (
        ('P', 'Para adoção'),
        ('A', 'Adotado'),
    )
    foto = models.ImageField(upload_to='fotos_pets')
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, choices= choices_status)

    def __str__(self):
        return self.nome
