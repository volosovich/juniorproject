from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView, FormView 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Product, Category
from datetime import datetime, timedelta


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


class ProductPage24h(ListView):
    model = Product
    template_name = 'product24h.html'
    context_object_name = 'products24h'

    def get_queryset(self):
        return Product.objects.filter(created_at__gte=datetime.now()-timedelta(days=1))


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

# OK registration block. May the Force be with me

class RegistrationForm(FormView):
    form_class = UserCreationForm
    success_url = '/products/login/'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationForm, self).form_valid(form)

class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/products/products24h/'
    
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginForm, self).form_valid(form)

