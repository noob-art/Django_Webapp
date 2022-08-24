from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm



# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            form.save()
            return redirect('blog-home')
        else:
            messages.error(request, "user not created")
            #return redirect('register')
            form = UserRegisterForm()
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})