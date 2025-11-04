from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm): #inheriting the UserCreationForm
    email=forms.EmailField()

    class Meta:  #Meta is basically configurations binded together
        model= User #specifiying what model the form should interact with, when form.save() runs, it will know it has to save into User model
        fields=['username','email','password1','password2'] #the order of the fields to be shown

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:  
        model= User 
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']