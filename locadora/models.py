from django.db import models

# Create your models here.
class Categoria (models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Locacao (models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Filme (models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    locacao = models.ManyToManyField (Locacao)

    def __str__(self):
        return self.titulo

