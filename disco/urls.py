from django.urls import path
from .views import list_musicas, new_musicas, del_musicas, update_musicas

app_name = 'disco'

urlpatterns = [
    path('list_musicas/', list_musicas, name="list_musicas"),
    path('new_musicas/', new_musicas, name="new_musicas"),
    path('update_musicas/<int:id>/', update_musicas, name="update_musicas"),
    path('del_musicas/<int:id>/', del_musicas, name="del_musicas"),
]