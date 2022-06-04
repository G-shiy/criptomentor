from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

time = [
    ('01', '5'),
    ('02', '10'),
    ('03', '15'),
    ('04', '20'),
]

tipo = [
    ('text', 'text'),
    ('analise', 'analise'),
    ('curso', 'curso'),
]


class Usuario(AbstractUser):
    email: str = models.EmailField(unique=True, blank=False)
    password: str = models.CharField(max_length=95, blank=False)
    is_staff = models.BooleanField(default=False, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)
    username: str = models.CharField(max_length=50)
    tel: str = models.CharField(max_length=18, blank=True)
    data_nascimento: int = models.DateField()
    cpf: str = models.CharField(max_length=15, unique=True)
    pfp = models.ImageField(blank=True, null=True)
    created_at: float = models.DateField(default=datetime.now)
    premium: bool = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'premium', 'tel', 'is_staff', 'is_superuser']

    def __str__(self) -> str:
        return self.name


class Text(models.Model):
    text = models.TextField(blank=False, null=False, editable=True)
    time = models.CharField(blank=True, null=False, editable=True, choices=time, max_length=3)
    types = models.CharField(choices=tipo, max_length=8, blank=True)
    title = models.CharField(blank=False, null=False, editable=True, max_length=25)
    imagem = models.ImageField(blank=True, null=False)
    thumbnail = models.ImageField(blank=False, null=False)
    created_at = models.DateField(default=datetime.now)
    video = models.URLField(blank=False, null=False)
    theme = models.CharField(blank=False, null=False, max_length=35)

    def __str__(self) -> str:
        return self.text


'''
class Curso(models.Model):
  text = models.TextField(blank=False,null=False, editable=True)
  title = models.CharField(blank=False, null=False, editable=True, max_length=25)
  time = models.CharField(blank=True, null=False, editable=True, choices=time, max_length=3)
  imagem = models.ImageField()
  thumbnail = models.ImageField(blank=True, null=False)
  created_at = models.DateField(default=datetime.now)
  video = models.URLField(blank=False, null=False)
  theme = models.CharField(blank=False, null=False, max_length=10) # voltar aqui depois
  def __str__(self) -> str:
      return self.text

class Analise(models.Model):
  text = models.TextField(blank=False,null=False, editable=True)
  title = models.CharField(blank=False, null=False, editable=True, max_length=25)
  imagem = models.ImageField()
  thumbnail = models.ImageField(blank=False, null=False)
  created_at = models.DateField(default=datetime.now)
  video = models.URLField(blank=False, null=False)
  theme = models.CharField(blank=False, null=False, max_length=10) # voltar aqui depois
  def __str__(self) -> str:
      return self.text
      
'''
