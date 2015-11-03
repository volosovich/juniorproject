from .views import TestPage
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', TestPage.as_view(), name = 'index'),
]
#url(r'^$', TestPage.as_view(), name = 'index')
