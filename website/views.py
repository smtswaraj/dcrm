from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user  = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "you Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was an Error Login In, Please Try Again.....")
            return redirect('home')
    else:
        return render(request, 'home.html', {"message":messages})
def login(request):
    pass
def logout(request):
    pass
