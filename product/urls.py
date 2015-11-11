from .views import ProductPage, CategoryAllPage, CategoryPage, ProductPage24h, RegistrationForm, LoginForm, LogoutForm
from django.conf.urls import include, url

urlpatterns = [
#    url(r'^category/', CategoryPage.as_view(), name = 'categories'),
#    url(r'^', ProductPage.as_view(), name = 'products'),
#    url(r'^category/', CategoryPage.as_view(), name = 'categories'),

    url(r'^$', CategoryAllPage.as_view(), name = 'categoryall'),
    url(r'^products24h/', ProductPage24h.as_view(), name = 'products24h'),
    url(r'^registr/$', RegistrationForm.as_view()),
    url(r'^login/$', LoginForm.as_view()),
    url(r'^logout/$', LogoutForm.as_view()),
    url(r'^([-\w]+)/$', CategoryPage.as_view(), name = 'category'),
    url(r'^(?P<test111>[-\w]+)/(?P<slug>[-\w]+)/$', ProductPage.as_view(), name = 'products'),

]

#    url(r'^registr/', RegistrationForm.as_view(), name = 'registr'),
