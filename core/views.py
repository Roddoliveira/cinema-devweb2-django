from calendar import c
from nis import cat
from typing import List
#from socket import fromshare

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
#from html5lib import serialize

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework import status
from core.models import categoria, compra, diretor, filme
from core.models import produtora

import json

@method_decorator (csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = categoria.objects.get(id=id)
            data = {}
            data ['id'] = qs.id
            data ['descricao'] = qs.descricao
            return JsonResponse(data)
        else:
            data = list(categoria.objects.values())
            formatted_data=json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")


    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao":nova_categoria.descricao}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = categoria.objects.get(id=id)
        qs.descricao = json_data['descricao'] #if 'descricao' in json_data else qs.descricao
        qs.save()
        data = {}
        data['id'] = qs.id
        data ['descricao'] = qs.descricao
        return JsonResponse(data)

    def delete(self, request, id):
        qs = categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem': "Item excluído com sucesso"}
        return JsonResponse(data)



class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = categoria
        fields = '__all__'


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

class CategoriasListGeneric(ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoraSerializer(ModelSerializer):
    class Meta:
        model = produtora
        fields = '__all__'

class ProdutoraViewSet(ModelViewSet):
    queryset = produtora.objects.all()
    serializer_class = ProdutoraSerializer

class FilmeSerializer(ModelSerializer):
    class Meta:
        model = filme
        fields = '__all__'

class FilmeViewSet(ModelViewSet):
    queryset = filme.objects.all()
    serializer_class = FilmeSerializer

class DiretorSerializer(ModelSerializer):
    class Meta:
        model = diretor
        fields = '__all__'

class DiretorViewSet(ModelViewSet):
    queryset = diretor.objects.all()
    serializer_class = DiretorSerializer

class CompraSerializer(ModelSerializer):
    class Meta:
        model = compra
        fields = '__all__'


class CompraViewSet(ModelViewSet):
    queryset = compra.objects.all()
    serializer_class = CompraSerializer