from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from rango.models import Category, Page

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

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        # Query DB category entries for match slug = category_name_slug
        # will return one model instance, or raise exception
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all associated pages, return as list of page obj. or empty list
        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage' : 'This tutorial has been put together by Martin.'}
    return render(request, 'rango/about.html', context=context_dict)