from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from user.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from product.models import Product


def index(request):
    goods = Product.objects.all().order_by('pk')
    return render(request, 'index.html', {'email': request.session.get('user'), 'goods':goods})


class RegisterView(FormView):
    template_name = 'register.html'  # template_name이라고 하면 html파일이조? 이게 부모인 FormView에서 가져온거에요.
    form_class = RegisterForm  # 위의 임포트든 된것을 form_class의 값으로 할당해줌.
    success_url = '/jwy'  # 회원가입이 정상적으로 된 경우 해당 url로 화면 전환이 이루어짐


class LoginView(FormView):
    template_name = 'login.html'  # template_name이라고 하면 html파일이조? 이게 부모인 FormView에서 가져온거에요.
    form_class = LoginForm
    success_url = '/jwy'

    # LoginView.as_view()가 실행될 때
    def form_valid(self, form):  # form유효성(데이터가 정상일때)을 마쳤을 때 사용해요. 로그인이 정상적으로 되었는 경우!
        self.request.session['user'] = form.email  # sessuib에 키값 user를 생성하는데요. 그 값은 form의 email속성에서 가져다와요.

        return super().form_valid(form)  # 부모클래스 FormView에 있는 form_valid()메소드를 호출합니다.

def logoutview(request):
    logout(request)
    return redirect('/jwy')