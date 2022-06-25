from webbrowser import get
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm
from django.contrib.auth import get_user_model



def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method != 'POST':
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        else:
            return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method != 'POST':
            form = SignUpForm()
            return render(request, 'accounts/signup.html', {'form':form})
        else:
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
    else:
        return redirect('/')

def test_view(request):
    users = get_user_model().objects.all()
    return render(request, 'accounts/test.html', {'users': users})
