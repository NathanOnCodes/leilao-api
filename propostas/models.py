import datetime
from django.db import models
from produtos.models import Produtos
from usuarios.models import Usuarios

class Propostas(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    autor = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_da_proposta = models.DateTimeField(default=datetime.datetime.now)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name="produtos")
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name="usuarios")


    def __str__(self):
        return f"Proposta de {self.autor} para o produto {self.produto}"

    