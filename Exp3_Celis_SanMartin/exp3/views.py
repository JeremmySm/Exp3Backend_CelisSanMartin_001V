from django.shortcuts import render, redirect
from .models import Usuariomoroso, Usuario
from .forms import morosoForm


# Create your views here.
def index4(request):
    usuariomorosos = Usuariomoroso.objects.all()   

    return render(request, 'index4.html', context={'usuariomorosos':usuariomorosos})    

def index2(request):
    if request.method=='POST': 
        usuariomoroso=morosoForm(request.POST)
        if usuariomoroso.is_valid():
            usuariomoroso.save()         #metodo que crea un nuevo objeto, reemplaza al insert
            return redirect('index4')
    else: 
        usuariomoroso=morosoForm()
    return render(request, 'index2.html', {'usuariomoroso': usuariomoroso})   

def index(request):

    return render (request, 'index.html')

def index3(request):

    return render (request, 'index3.html')

def index5(request,id):
    usuariomoroso = Usuariomoroso.objects.get(idmoroso=id)
    
    datos = {
        'form': morosoForm(instance=usuariomoroso)
    }
    if request.method == 'POST': 
        formulario = morosoForm(data=request.POST, instance = usuariomoroso)
        if formulario.is_valid: 
            formulario.save()           #permite actualizar la info del objeto encontrado
            return redirect('index4')
        else:
            usuariomoroso=morosoForm()
            return render(request,'index')
    return render(request, 'index5.html',datos)
    
def index6(request,id):
    usuariomoroso = Usuariomoroso.objects.get(idmoroso=id)
    usuariomoroso.delete()
    return redirect('index4')