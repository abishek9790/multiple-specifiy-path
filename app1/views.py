from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def funa(request):
    return HttpResponse(" project 8 app1 fun1")
def funb(request):
    return HttpResponse("project 8 app1 fun2")