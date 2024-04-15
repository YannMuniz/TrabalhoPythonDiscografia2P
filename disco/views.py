from django.shortcuts import render, redirect
from .models import Albuns, Musicas, Bandas
from .forms import MusicasForm
# Create your views here.

def list_musicas(request):
    musicas = Musicas.objects.all()
    template_name = 'list_musicas.html'
    context = {
        'musicas' : musicas
    }
    return render(request, template_name, context)

def new_musicas(request):
    if request.method == 'POST':
        form = MusicasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disco:list_musicas')
    else:
        template_name = 'new_musicas.html'
        context = {'form' : MusicasForm()}
        return render(request, template_name, context)

def update_musicas(request, id):
    musicas = Musicas.objects.get(id=id)
    print(musicas)
    if request.method == 'POST':
        form = MusicasForm(request.POST, instance=musicas)
        if form.is_valid():
            form.save()
            return redirect('disco:list_musicas')
    else:
        template_name = 'update_musicas.html'
        context = {
            'form' : MusicasForm(instance=musicas),
            'id' : id
        }
        return render(request, template_name, context)


def del_musicas(request, id):
    musicas = Musicas.objects.get(id=id)
    musicas.delete()
    return redirect('disco:list_musicas')