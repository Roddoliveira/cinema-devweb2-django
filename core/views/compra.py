from core.models import compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer
from rest_framework.viewsets import ModelViewSet


class CompraViewSet(ModelViewSet):
    queryset = compra.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        return CriarEditarCompraSerializer

    def get_queryset(self):
        usuario = self.request.user
        if usuario.groups.filter(name="Administradores"):
            return compra.objects.all()
        return compra.objects.filter(usuario=usuario)
