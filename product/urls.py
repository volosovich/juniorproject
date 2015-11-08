from .views import ProductPage, CategoryAllPage, CategoryPage
from django.conf.urls import include, url

urlpatterns = [
#    url(r'^category/', CategoryPage.as_view(), name = 'categories'),
#    url(r'^', ProductPage.as_view(), name = 'products'),

#    url(r'^category/', CategoryPage.as_view(), name = 'categories'),





    url(r'^$', CategoryAllPage.as_view(), name = 'categoryall'),
    url(r'^([-\w]+)/$', CategoryPage.as_view(), name = 'category'),
    url(r'^(?P<test111>[-\w]+)/(?P<slug>[-\w]+)/$', ProductPage.as_view(), name = 'products'),


]
