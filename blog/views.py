from django.shortcuts import render #loads HTML template with data and returns it as a web response
from .models import Post # the dot before models is used as the models file is in the same directory(package)

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render (request,'blog/home.html',context) #parameters are requst (HTTP request sent by user's browser to build the response properly), template (the HTML file you want to display) path, context(Python dictionary that u want to send to the file, only a single dictionary)

def about(request):
    return render (request,'blog/about.html',{'title':'About'})



