from .views import ProductPage, CategoryPage
from django.conf.urls import include, url

urlpatterns = [
#    url(r'^$', TestPage.as_view(), name = 'index'),
    url(r'^category/', CategoryPage.as_view(), name = 'categories'),
    url(r'^', ProductPage.as_view(), name = 'products'),
#    url(r'^category/', CategoryPage.as_view(), name = 'categories')
]
#url(r'^$', TestPage.as_view(), name = 'index')
