from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rango.models import Category

def redir(request):
    return redirect('/rango')


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    # Create a context dictionairy to give context to {{ msg }} template variables in the html file
    # Usage : for {{msgname}} in html >>> 'msgname' : 'msgcontent' for each key : value pair
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    # Return our rendered response
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'boldmessage' : 'This tutorial has been put together by Martin.'}
    return render(request, 'rango/about.html', context=context_dict)