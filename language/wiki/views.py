from django.shortcuts import render
from wiki.models import Category, Page
# Create your views here.

def wiki(request):
    categories = Category.objects.order_by('-likes')
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html',context)


def about(request):
    return render(request, 'wiki/about.html')


 
def category(request, categoryName):
    context = {}
    try:
        category = Category.objects.get(name=categoryName)
        context['category'] = category
        pages = Page.objects.filter(category=category)
        context['pages'] = pages
    except Category.DoesNotExist:
        pass
    return render(request, 'wiki/category.html', context)