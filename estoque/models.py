from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    fornecedor = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome

    def estoque_baixo(self):
        return self.quantidade < 5  # Define um alerta de estoque baixo
