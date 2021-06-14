from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
  retrunobject = HttpResponse('<h1>hello world</h1>')
  return retrunobject

class HelloWorldView(TemplateView):
  template_name = 'hello.html'
