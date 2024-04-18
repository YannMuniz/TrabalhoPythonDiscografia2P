from django.urls import path
from .views import musica_list, musica_new, musica_delete, musica_edit

app_name = 'disco'

urlpatterns = [
    path('musica_list/', musica_list, name="musica_list"),
    path('musica_new/', musica_new, name="musica_new"),
    path('musica_edit/<int:id>/', musica_edit, name="musica_edit"),
    path('musica_delete/<int:id>/', musica_delete, name="musica_delete"),
]