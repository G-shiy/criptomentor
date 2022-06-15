from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.backends import TokenBackend
from userAuth.models import Text, Usuario
from userAuth.pagination import FilterResults
from userAuth.serializer import TextSerializer, UsuarioSerializer, LoginSerializer

class GetAuthenticatedUser(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        return self.request.user

class CreateUser(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ListUser(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class listUserId(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UpdateUser(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class DestroyUser(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class TextviewSet(viewsets.ModelViewSet):
    """EXIBINDO TODOS OS TEXTOS"""
    queryset = Text.objects.all()
    serializer_class = TextSerializer
    pagination_class = FilterResults


"""class CursoviewSet(viewsets.ModelViewSet):
  EXIBINDO TODOS OS CURSOS
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer

class AnaliseviewSet(viewsets.ModelViewSet):
  EXIBINDO TODOS AS ANALISES
  queryset = Analise.objects.all()
  serializer_class = AnaliseSerializer"""
