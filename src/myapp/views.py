from django.views.generic import TemplateView
from .tasks import show_hello_world
from .models import DemoModel
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, get_list_or_404
# Create your views here.
from .models import Question


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
    taiSan = ['maytinh', 'dien thoai', 'test_1', 'test_2']
    context = {
        'name' : 'test_name',
        'taiSan': taiSan
    }
    return render(request, 'myapp/index.html', context)

def viewlist(request):
    # list_question = get_list_or_404(Question, pk=1) # pk=2 tìm khóa chính(id) = 2
    # list_question = get_list_or_404(Question, question_text='Bạn bao nhiêu tuỏi')
    list_question = Question.objects.all()
    context = {"data": list_question}
    return render(request, 'myapp/question_list.html', context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    # q = get_list_or_404(Question, pk=question_id)
    context = {
        'qs': q
    }
    return render(request, 'myapp/detail_question.html', context)
