from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from .models import Product, Category



#class TestPage(ListView):
#    model = TestforPage
#    template_name = 'test-page.html'

class ProductPage(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name ='products'

class CategoryPage(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'categories'
