from django.shortcuts import render


def index(request):
    return render(request, 'view/index.html') 
# Create your views here.
