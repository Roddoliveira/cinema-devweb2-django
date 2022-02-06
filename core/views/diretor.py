from core.models import diretor
from core.serializers import DiretorSerializer
from rest_framework.viewsets import ModelViewSet


class DiretorViewSet(ModelViewSet):
    queryset = diretor.objects.all()
    serializer_class = DiretorSerializer