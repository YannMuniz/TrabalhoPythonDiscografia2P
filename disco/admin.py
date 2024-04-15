from django.contrib import admin
from .models import Albuns, Bandas, Musicas

admin.site.register(Albuns)
admin.site.register(Musicas)
admin.site.register(Bandas)