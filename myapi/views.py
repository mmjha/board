from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login
from user.views import UserViewSet

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_logged_in.disconnect(update_last_login, dispatch_uid='update_last_login')
            login(request, user)
            return redirect('/api/board')
            # return render(request, 'index.html', {'username': username})
        else:
            return redirect('/?fail')
    else:
        if not request.user or not request.user.is_authenticated:
            return render(request, 'login.html')
        else:
            return redirect('/api/board')
            # return render(request, 'index.html', {'username': request.user})