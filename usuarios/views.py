from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.

def cadastro(request):
    template_name = 'usuarios/cadastro.html'

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    
    if request.method == 'GET':
        
        return render(request, template_name)
    elif request.method == 'POST':
    
        nome    = request.POST.get('nome')
        email   = request.POST.get('email')
        senha   = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
       
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            messages.add_message(request, constants.WARNING,
                                 'Todos os campos são de prenchimentos obrigatórios')
            return render(request, template_name)
        
        if senha != confirmar_senha:
            messages.add_message(request, constants.WARNING,
                                 'A senha e confirmar senha são diferentes')
            return render(request, template_name)
        
        else:
            try:
                usuario = User.objects.create_user(
                    username=nome, email=email, password=senha)
                usuario.save()
                messages.add_message(request, constants.SUCCESS,
                                     'Cadastro realizado com sucesso')
                return render(request, template_name)
                
                #return HttpResponse(f'{nome}, {email}, {senha}, {confirmar_senha}')
            except:
              messages.add_message(request, constants.ERROR,
                                   'Erro ao cadastrar, tente novamente mais tarde')
              return render(request, template_name)
            

def login_user(request):
    template_name = 'usuarios/login.html'
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'GET':
        return render(request, template_name)
    
    elif request.method == 'POST':

        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(username = nome, password = senha)

        if user is not None:
            login(request, user)
            print('usuario logado')
            return redirect('/divulgar/novo_pet')
         
          
        else:
            messages.add_message(request, constants.ERROR,
                              'Usuario não localizado.')
            return render(request, template_name)
        
def sair(request):
    template_name = 'usuarios/login.html'
    logout(request)
    return render(request, template_name)
            


           
