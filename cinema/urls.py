from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core import views

router = routers.DefaultRouter()
router.register(r"categoria", views.CategoriaViewSet)
router.register(r"produtoras", views.ProdutoraViewSet)
router.register(r"filmes", views.FilmeViewSet)
router.register(r"diretores", views.DiretorViewSet)
router.register(r"compras", views.CompraViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    # Open API 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    #Autenticação
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #Outros endpoints
    path("categorias/", views.CategoriaView.as_view()),
    path("categorias/<int:id>/", views.CategoriaView.as_view()),
    path("categorias-apiview/", views.CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    path("categorias-generic/", views.CategoriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()),
    path("", include(router.urls)),
]
