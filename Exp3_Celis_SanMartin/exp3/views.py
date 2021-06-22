from django.shortcuts import render

# Create your views here.

def index(request):

    return render (request, 'index.html')

def index3(request):

    return render (request, 'index3.html')