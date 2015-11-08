from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView 
from .models import Product, Category



#class TestPage(ListView):
#    model = TestforPage
#    template_name = 'test-page.html'

class ProductPage(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'

    def get_queryset(self):
        self.filter_category_slug = get_object_or_404(Category, slug=self.kwargs['test111'])
        self.filter_product_slug = get_object_or_404(Product, slug=self.kwargs['slug'])
#        return Product.objects.filter(category_for_product = self.filter_category_slug, slug = self.filter_product_slug)
        return Product.objects.filter(category_for_product = self.filter_category_slug)



class CategoryAllPage(ListView):
    model = Category
    template_name = 'categoryall.html'
    context_object_name = 'categoriesall'


class CategoryPage(ListView):
    model = Product
    template_name = 'category.html'
#    slug_field = 'category_for_product' 
    context_object_name = 'categories'
#    queryset = Product.objects.filter(category_for_product__slug = 'macapple')

    def get_queryset(self):
        self.filter = get_object_or_404(Category, slug = self.args[0])
        return Product.objects.filter(category_for_product = self.filter)


#class CategoryPage(DetailView):
#    model = Category
#    template_name = 'category.html'
#    context_object_name = 'categories'


