from dataclasses import fields
from email.policy import default
from django.forms import CharField
from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from core.models import categoria
from core.models import produtora
from core.models import filme
from core.models import diretor
from core.models import compra
from core import models
from core.models import itenscompra
from rest_framework import serializers


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = "__all__"


# class CategoriaDetailSerializer(ModelSerializer):
# class Meta:
# model = categoria
# fields = "__all__"
# depth = 1


class ProdutoraSerializer(ModelSerializer):
    class Meta:
        model = produtora
        fields = "__all__"


class ProdutoraNestedSerializer(ModelSerializer):
    class Meta:
        model = produtora
        fields = ("nome",)


class FilmeSerializer(ModelSerializer):
    class Meta:
        model = filme
        fields = "__all__"


class FilmeDetailSerializer(ModelSerializer):
    categoria = CharField(source="categoria.descricao")
    diretores = SerializerMethodField()
    produtora = ProdutoraNestedSerializer()

    class Meta:
        model = filme
        fields = "__all__"
        depth = 1

    def get_diretores(self, instance):
        nomes_diretores = []
        diretores = instance.diretores.get_queryset()
        for diretor in diretores:
            nomes_diretores.append(diretor.nome)
        return nomes_diretores


class DiretorSerializer(ModelSerializer):
    class Meta:
        model = diretor
        fields = "__all__"


class ItensComprasSerializer(ModelSerializer):
    class Meta:
        model = itenscompra
        fields = "__all__"


class ItensComprasSerializer(ModelSerializer):
    total = SerializerMethodField()

    class Meta:
        model = itenscompra
        fields = ("filme", "quantidade", "total")
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.filme.preco


class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email")
    status = SerializerMethodField()
    itens = ItensComprasSerializer(many=True)

    class Meta:
        model = compra
        fields = ("id", "status", "usuario", "itens", "total")

    def get_status(self, instance):
        return instance.get_status_display()


class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = itenscompra
        fields = ("filme", "quantidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = compra
        fields = ("usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compras = compra.objects.create(**validated_data)
        for item in itens:
            itenscompra.objects.create(compra=compras, **item)
        compras.save()
        return compras

    def update(self, instance, validate_data):
        itens = validate_data.pop("itens")
        if itens:
            instance.itens.all().delete()
            for item in itens:
                itenscompra.objects.create(compra=instance, **item)
            instance.save()
        return instance
