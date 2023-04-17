from django.views.generic import TemplateView
from .tasks import show_hello_world
from .models import DemoModel
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
# Create your views here.


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo_content'] = DemoModel.objects.all()
        return context

def index_view(request):
    return HttpResponse('xin chao')

class IndexView(View):
    def get(self, request): # class nên cần phải có self
        return HttpResponse('ham get')

    def post(self, request):
        return HttpResponse('ham post')

def tester(request):
    taiSan = ['maytinh', 'dien thoai']
    context = {
        'name' : 'test_name',
        'taiSan': taiSan
    }
    return render(request, 'myapp/index.html', context)


