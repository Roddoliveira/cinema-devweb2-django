from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'categorias-viewset', views.CategoriaViewSet)
router.register(r'produtoras', views.ProdutoraViewSet)
router.register (r'filmes', views.FilmeViewSet)
router.register(r'diretores', views.DiretorViewSet)
router.register(r'compras', views.CompraViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/',views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
    path('', include(router.urls))

]
