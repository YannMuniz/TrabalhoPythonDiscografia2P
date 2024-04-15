from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'index.html'
    context = {"mensagem": "Músicas"}
    return render(request, template_name)
