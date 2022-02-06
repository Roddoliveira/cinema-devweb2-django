from core.models import compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer
from rest_framework.viewsets import ModelViewSet


class CompraViewSet(ModelViewSet):
    queryset = compra.objects.all()
    #serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        return CriarEditarCompraSerializer