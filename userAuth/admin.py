from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userAuth.models import Text, Usuario


class Usuarios(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'cpf', 'created_at', 'premium']
    list_display_links = ['id', 'email', 'username']
    search_fields = ['username', 'email', 'id', 'cpf']
    list_per_page = 15


admin.site.register(Usuario, Usuarios)


"""class Analises(admin.ModelAdmin):
  list_display = ['title', 'theme' ,'created_at']
  list_display_links = ['title', 'theme']
  search_fields = ['title']

admin.site.register(Analise, Analises)

class Cursos(admin.ModelAdmin):
  list_display = ['title', 'theme' ,'created_at']
  list_display_links = ['title', 'theme']
  search_fields = ['title'] 

admin.site.register(Curso, Cursos)"""


class Texts(admin.ModelAdmin):
    list_display = ['title', 'theme', 'created_at']
    list_display_links = ['title', 'theme']
    search_fields = ['title']


admin.site.register(Text, Texts)
