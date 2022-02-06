from core.models import categoria
from core.serializers import CategoriaSerializer
from rest_framework.viewsets import ModelViewSet


class CategoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
