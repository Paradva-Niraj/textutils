# file created by admin for redirection a pages

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'nicxx'}
    return render(request,'index.html',params)
    # return HttpResponse("<h2>hello from nicxx</h2>")

def removepunc(request):
    return HttpResponse("<h3>from punc</h3>")
    
def capitalizefirst(request):
    return HttpResponse("<h3>from capitalize</h3>")
    
def newlineremove(request):
    return HttpResponse("<h3>from newlineremover</h3>")
    
def spaceremove(request):
    return HttpResponse("<h3>spaceremove</h3>")
    
def charcount(request):
    return HttpResponse("<h3>from char count</h3>")

