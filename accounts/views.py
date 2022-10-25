from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import RegisterForm, LoginForm

class RegisterView(CreateView):
    form_class =  RegisterForm
    template_name = 'auth/register.html'
    success_url = '/'

def loginpage(request):
    form = LoginForm(request.POST or None)

    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('homepage')
    context = {
        "form": form
        }
    return render(request, "auth/login.html", context)