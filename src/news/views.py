from django.shortcuts import render
from django.http import HttpResponse
from .form import PostForm, SendEmail
from django.views import View

# Create your views here.

class IndexClass(View): # kế thừa từ View
    def get(self, request):
        return HttpResponse('news index')

class ClassSaveNews(View):
    def get(self, request):
        a = PostForm()
        context = { 'f': a }
        return render(request, 'news/add_news.html', context)

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse('luu ok')
        else:
            return HttpResponse('khong duoc validate')
    def put(self):
        pass

    def patch(self):
        pass

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', { 'f': b })

def process(request):
    if request.method == 'POST':
        m = SendEmail(request.POST) 
        if m.is_valid():
            tieude = m.cleaned_data['title']
            cc = m.cleaned_data['cc'] # cc có nghĩa là có gửi 1 bản đính kèm cho người khác hay không
            noidung = m.cleaned_data['content']
            email = m.cleaned_data['email']

            context = { # có thể gửi cả m sang
                'td': tieude, 
                'c': cc,
                'b': noidung,
                'd': email
            }
            
            return render(request, 'news/print_email.html', context)
        
        else:
            return HttpResponse('khong duoc validate')
    else:
        return HttpResponse('send mail fail')