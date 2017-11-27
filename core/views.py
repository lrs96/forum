from django.shortcuts import render, redirect
from core.forms import NovoTopicoForm, PostForm
from core.models import NovoTopico, Post
# Create your views here.

def index(request):
    contexto = {
        'title': 'Fórum'
    }
    return render(request, 'index.html', contexto)

def topico(request):
    if request.POST:
        novo = NovoTopicoForm(request.POST)
        if novo.is_valid():
            novo.save()
            redirect ('topic.html')
    else:
        novo = NovoTopicoForm
    contexto = {
        'title':'Novo tópico'
    }
    return render(request,'novo-post.html', contexto)

def post(request):
    if request.POST:
        novo = PostForm(request.POST)
        if novo.is_valid():
            novo.save()
    else:
        novo = PostForm
    contexto = {
        'title': 'Post',
        'post': Post.objects.all()
    }
    return render(request, 'post.html', contexto)

def topic(request):
    contexto = {
        'title': 'Tópico',
        'topico':NovoTopico.objects.all()
    }
    return render(request, 'topic.html', contexto)