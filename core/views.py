from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request,nome,n1,n2):
    soma = n1+n2
    return HttpResponse("<h1>E AI {}  {}</h1>".format(nome,soma))