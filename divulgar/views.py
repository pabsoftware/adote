from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




# Create your views here.
@login_required
def novo_pet(request):
    template_name = 'divulgar/novo_pet.html'
    if request.method == 'GET': 
        return render(request, template_name)
    
    elif request.method == 'POST':
        
        return render(request, template_name)
