from userAuth.views import TextviewSet, GetAuthenticatedUser, AnaliseviewSet, NoticiaviewSet
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)


base = "api/v1/"
router = routers.DefaultRouter()

router.register('Noticia', NoticiaviewSet, basename='noticia')
router.register('analise', AnaliseviewSet, basename='analise')
router.register('texts', TextviewSet, basename='texts')
router.register('GetAuthenticatedUser', GetAuthenticatedUser, basename='GetAuthenticatedUser')

urlpatterns = [
    path('criptomentor-geral/', admin.site.urls),
    path(f'{base}', include(router.urls)),
    path(f'{base}', include('userAuth.urls')),
    path(f'{base}docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{base}docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{base}docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path(f'{base}token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{base}token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
