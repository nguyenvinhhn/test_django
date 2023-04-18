from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User

# Create your views here.

class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Index Login</h1>')
    
class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        username = request.POST.get('tendangnhap')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=username, password=matkhau)
        if my_user is None:
            return HttpResponse('User not found')

        # login(request, my_user)
        # data = "user =  %s, password = %s." % (username, matkhau)
        # return HttpResponse(data)
        return render(request, 'Login/thanhcong.html')

class ViewUser(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponse('ban vui long dang nhap')
        else:
            return HttpResponse('day la view user')

@decorators.login_required(login_url='/login/') # phải login trước khi vào view_product
def view_product(request):
    return HttpResponse('xem san pham')