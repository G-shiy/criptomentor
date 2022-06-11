from django.urls import path
from .views import CreateUser, UserRetrieveUpdate, listUserId, DestroyUser, UpdateUser, ListUser, LoginAPIView

urlpatterns = [
    path('createUser', CreateUser.as_view()),
    path('users', ListUser.as_view()),
    path('updateUser/<int:pk>', UpdateUser.as_view()),
    path('deleteUser/<int:pk>', DestroyUser.as_view()),
    path('listUserId/<int:pk>', listUserId.as_view()),
    path('userRetrieveUpdate/<int:pk>', UserRetrieveUpdate.as_view()),
    path('GetAuthenticatedUser/<int:pk>', LoginAPIView.as_view()),
]
