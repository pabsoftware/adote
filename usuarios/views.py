from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    if request.method == 'GET':
        
        return render(request, template_name)
    elif request.method == 'POST':
    
        nome    = request.POST.get('nome')
        email   = request.POST.get('email')
        senha   = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
       
        if senha != confirmar_senha:
            return render(request, template_name)

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            return HttpResponse('Todos os campos são de preenchimento obrigatorio') 
        
        else:
            return render(request, template_name)
            #return HttpResponse(f'{nome}, {email}, {senha}, {confirmar_senha}')
