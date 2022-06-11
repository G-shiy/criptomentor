from django.urls import path
from .views import CreateUser, UserRetrieveUpdate, listUserId, DestroyUser, UpdateUser, ListUser, GetAuthenticatedUser

urlpatterns = [
    path('createUser', CreateUser.as_view()),

]
