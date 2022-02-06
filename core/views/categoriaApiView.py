from core.models import categoria
from core.serializers import CategoriaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



class CategoriasList(APIView):
    def get(self, request):
        categorias = categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriaDetail(APIView):
    def get(self, request, id):
        categorias = get_object_or_404(categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categorias)
        return Response(serializer.data)

    def put(self, request, id):
        categorias = get_object_or_404(categoria.objects.all(), id=id)
        serializer = CategoriaSerializer(categorias, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        categorias = get_object_or_404(categoria.objects.all(), id=id)
        categorias.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
