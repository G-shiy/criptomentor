from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from userAuth.models import Text, Usuario
from django.contrib import auth
import jwt
from userAuth.pagination import FilterResults
from userAuth.serializer import TextSerializer, UsuarioSerializer, LoginSerializer
from django.conf import settings

class GetAuthenticatedUser(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UsuarioSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
