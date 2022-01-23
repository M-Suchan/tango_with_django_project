from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def redir(request):
    return redirect('/rango')


def index(request):
    # Create a context dictionairy to give context to {{ msg }} template variables in the html file
    # Usage : for {{msgname}} in html >>> 'msgname' : 'msgcontent' for each key : value pair
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return our rendered response
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return HttpResponse("""Rango says here is the about page. <a href="/rango/">Index</a>""")