""" Users views  """

 # Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    """ login view.  """
    if request.method == 'POST':
        print('*' * 10)
        username = request.POST['username']
        password = request.POST['password']
        print('*' * 10)
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')            
        else:
            return render(request, 'users/login.html', {'error':'INVALIDO USUARIO O PASSWORD'})
    return render(request, 'users/login.html')
