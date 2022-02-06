from core.models import filme
from core.serializers import FilmeSerializer, FilmeDetailSerializer
from rest_framework.viewsets import ModelViewSet


class FilmeViewSet(ModelViewSet):
    lookup_field = 'id'
    queryset = filme.objects.all()
    #serializer_class = FilmeSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return FilmeDetailSerializer
        if self.action == "retrieve":
            return FilmeDetailSerializer
        return FilmeSerializer
