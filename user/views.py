from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from user.forms import RegisterForm

def index(request):
    return render(request,'index.html')
def join(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/admin')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form' : form })
