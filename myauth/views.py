from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from . forms import RegisterForm


# Create your views here.


def testa(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def registerUser(request):
    form = RegisterForm()
    form.fields['password1'].widget.attrs['class'] = "form-control forms-fonts"
    form.fields['password2'].widget.attrs['class'] = "form-control forms-fonts"

    if request.method == 'POST':
        postform = RegisterForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('login')
        else:
            messages.error(request, 'Error Adding User')
    return render(request, 'auth_register.html', {'name': 'Brian Sagalla', 'form': form})


def loginUser(request):
    form = AuthenticationForm()
    form.fields['username'].widget.attrs['class'] = "form-control forms-fonts"
    form.fields['password'].widget.attrs['class'] = "form-control forms-fonts"

    if request.method == 'POST':
        postform = AuthenticationForm(request, data=request.POST)
        if postform.is_valid():
            user = postform.get_user()
            login(request, user)
            return redirect('listEmployees')
        else:
            logerror = postform.get_invalid_login_error()
            messages.error(request, logerror)

    return render(request, 'auth_login.html', {'name': 'Brian Sagalla', 'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


def testb(request):
    return render(request, 'login.html', {'name': 'Brian Sagalla'})
