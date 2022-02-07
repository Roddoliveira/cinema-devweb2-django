from django.db import models
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.
class categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class produtora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return self.nome


class diretor(models.Model):
    class Meta:
        verbose_name_plural = "Diretores"

    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class filme(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.FloatField()
    categoria = models.ForeignKey(
        categoria, on_delete=models.PROTECT, related_name="filmes"
    )
    produtora = models.ForeignKey(
        produtora, on_delete=models.PROTECT, related_name="filmes"
    )
    diretores = models.ManyToManyField(diretor, related_name="filmes")

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.produtora)


class compra(models.Model):
    class statuscompra(models.IntegerChoices):
        Carrinho = 1, "Carrinho"
        Realizado = 2, "Realizado"
        Pago = 3, "Pago"

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    status = models.IntegerField(
        choices=statuscompra.choices, default=statuscompra.Carrinho
    )

    def __str__(self):
        return "%s (%s)" % (self.status, self.usuario)

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F("quantidade") * F("filme__preco"))
        )
        return queryset["total"]


class itenscompra(models.Model):
    compra = models.ForeignKey(compra, on_delete=models.CASCADE, related_name="itens")
    filme = models.ForeignKey(filme, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField()
