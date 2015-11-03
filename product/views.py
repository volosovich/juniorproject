from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from .models import TestforPage



class TestPage(ListView):
    model = TestforPage
    template_name = 'test-page.html'

#def main(request):
#    return render_to_response('', {})
