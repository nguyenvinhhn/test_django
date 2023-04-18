from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ManazineForm

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

        login(request, my_user)
        # data = "user =  %s, password = %s." % (username, matkhau)
        # return HttpResponse(data)
        return render(request, 'Login/thanhcong.html')

class ViewUser(LoginRequiredMixin, View): # lưu ý LoginRequireMixin phải đứng trước View
    login_url = '/login/' # kế thừa từ cha
    def get(self, request):
        # if not request.user.is_authenticated:
            # return HttpResponse('ban vui long dang nhap')
        # else:
        return HttpResponse('day la view user')

@decorators.login_required(login_url='/login/') # phải login trước khi vào view_product
def view_product(request):
    return HttpResponse('xem san pham')

class AddManazineClass(LoginRequiredMixin ,View):
    login_url = '/login/'
    def get(self, request):
        f = ManazineForm()
        context = { 'fm': f }
        return render(request, 'Login/add_manazine.html', context)

    def post(self, request):
        f = ManazineForm(request.POST)
        if not f.is_valid():
            return HttpResponse('ban nhap sai du lieu roi')

        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_magazine'): # cache reload database fix bug
            f.save()
            return HttpResponse('oke')
        else:
            return HttpResponse('you not have permission')
        
