from django.shortcuts import render, redirect
from .models import Musicas
from .forms import MusicasForm
# Create your views here.

def musica_list(request):
    musicas = Musicas.objects.all()
    template_name = 'musica_list.html'
    context = {
        'musicas' : musicas
    }
    return render(request, template_name, context)

def musica_new(request):
    if request.method == 'POST':
        form = MusicasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disco:musica_list')
    else:
        template_name = 'musica_new.html'
        context = {'form' : MusicasForm()}
        return render(request, template_name, context)

def musica_edit(request, id):
    musicas = Musicas.objects.get(id=id)
    print(musicas)
    if request.method == 'POST':
        form = MusicasForm(request.POST, instance=musicas)
        if form.is_valid():
            form.save()
            return redirect('disco:musica_list')
    else:
        template_name = 'musica_update.html'
        context = {
            'form' : MusicasForm(instance=musicas),
            'id' : id
        }
        return render(request, template_name, context)

def musica_delete(request, id):
    musicas = Musicas.objects.get(id=id)
    musicas.delete()
    return redirect('disco:musica_list')