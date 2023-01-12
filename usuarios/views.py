from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastro(request):
    template_name = 'cadastro.html'
    return render(request, template_name )
