from django.urls import path
from .views import CreateUser, UpdateUser
urlpatterns = [
    path('register/', CreateUser.as_view(), name='create_user'),
    path('update/', UpdateUser.as_view(), name="update_user")
]
