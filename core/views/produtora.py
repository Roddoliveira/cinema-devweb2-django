from core.models import produtora
from core.serializers import ProdutoraSerializer
from rest_framework.viewsets import ModelViewSet


class ProdutoraViewSet(ModelViewSet):
    queryset = produtora.objects.all()
    serializer_class = ProdutoraSerializer