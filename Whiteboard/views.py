from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


def homepage(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('loginpage')

def myinfopage(request):
    if request.user.is_authenticated:
        return render(request, "auth/infopage.html")
    else:
        return redirect('loginpage')

def list_user(request):
    model = User.objects.all().values()
    context = {
        'model':model
    }
    return render(request, 'auth/list_user.html', context)

def update(request, id):
    user = User.objects.get(id=id)
    context = {
        'user':user
    }
    return render(request, 'auth/update.html', context)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('list_user')

def updaterecord(request, id):
    newEmail = request.POST['email']
    newFirstName = request.POST['first_name']
    newLastName = request.POST['last_name']
    user = User.objects.get(id=id)
    user.email = newEmail
    user.first_name = newFirstName
    user.last_name = newLastName
    user.save()
    return redirect('list_user')