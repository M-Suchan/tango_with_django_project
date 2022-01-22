from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def redir(request):
    return redirect('/rango')
def index(request):
    return HttpResponse("""Rango says hey there partner! <a href="about">About.</a>""")
def about(request):
    return HttpResponse("""Rango says here is the about page. <a href="/rango">Index.</a>""")