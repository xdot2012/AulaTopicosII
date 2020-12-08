from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.base import TemplateView, View
from .forms import PessoaForm
from django.contrib import messages
from .models import Pessoa
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login as logon, logout




def login(request):
    return render(request,'login.html')



def do_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            logon(request, user)
            return redirect('primeira-view')
        else:
            messages.error(request,'Login ou Senha inválido!')
            return redirect('login')
    return render(request, 'login.html')



@login_required
def PrimeiraView(request):

    form = PessoaForm(request.POST or None)
    tipo_message = None
    pessoa = Pessoa.objects.filter().order_by('numero')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Formulário Salvo com sucesso!')
            tipo_message = 'S'
        else:
            tipo_message = 'E'
            messages.error(request,'Erro ao salvar fomulario')

    context = {
        'form': form,
        'tipo_message': tipo_message,
        'pessoa': pessoa, 
       
    }

    return render(request,'cadastros/primeira-view.html', context)


def EditView(request,pk):

    obj = Pessoa.objects.get(pk=pk)
    form = PessoaForm(request.POST or None, instance=obj)


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Formulário Editado com sucesso!')
            return redirect('primeira-view')
            
    context = {
       'pk': pk, 
       'form': form,
       
    }

    return render(request,'cadastros/edit_view.html', context)




def DeleteView(request,pk):

    obj = Pessoa.objects.get(pk=pk)
    obj.delete()
    messages.success(request,'Formulário Deletado com sucesso!')
    return redirect('primeira-view')
            









def Teste(request):


    context = {
       
       
    }

    return render(request,'cadastros/teste.html', context)









# class TESTE(View):



#     def get_template_names(self):
    
#     def post(self):

