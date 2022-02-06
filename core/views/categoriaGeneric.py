from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import categoria
from core.serializers import CategoriaSerializer

class CategoriasListGeneric(ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer