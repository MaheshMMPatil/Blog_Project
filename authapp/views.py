from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def registerView(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    context = {'form': form}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_urls')
    return render(request, template_name, context)


def loginView(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('u')
        pw = request.POST.get('p')

        user = authenticate(username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('frontpage')
    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('login_urls')

