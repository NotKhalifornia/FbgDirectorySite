from django.shortcuts import render, HttpResponse,redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def home_page(request):
    return HttpResponse("bishes")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})