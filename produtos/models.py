from django.db import models


class NegociacaoDoProduto(models.TextChoices):
    ABERTO = "ABERTO", "Aberto"
    FECHADO = "FECHADO", "Fechado"


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    negociacao_do_produto = models.CharField(
        choices=NegociacaoDoProduto.choices, default=NegociacaoDoProduto.ABERTO
    )
    data_leilao = models.DateField()
