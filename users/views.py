from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required #a decorator that mandates login to visit certain page
def register(request):
    if request.method== "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print("form valid")
            username= form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created. Please log in.")
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required #decorator- adds functionality to existing functions
def profile(request):
    return render(request,'users/profile.html')









