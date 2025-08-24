import datetime
from django.db import models

class NegociacaoDoProduto(models.TextChoices):
    ABERTO = "ABERTO", "Aberto"
    FECHADO = "FECHADO", "Fechado"


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    negociacao_do_produto = models.CharField(
        choices=NegociacaoDoProduto.choices, default=NegociacaoDoProduto.ABERTO
    )
    data_leilao = models.DateField()
    dono_do_produto = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        related_name="produtos",
    )

    def __str__(self):
        return self.nome
