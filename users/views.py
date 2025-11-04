from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
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
    if request.method== "POST":
        if 'remove_photo' in request.POST:
            request.user.profile.image="default.jpg"
            request.user.profile.save()
            return redirect('profile')
            messages.success(request, f"Your profile picture has been removed.")
        
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
            messages.success(request, f"Your profile has been updated.")
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'users/profile.html',context)









