from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from homeTests.models import questions
from homeTests.serializer import TestSerializer


class CreateProve(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = TestSerializer 


class ListUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = TestSerializer