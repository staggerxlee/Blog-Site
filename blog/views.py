from django.shortcuts import render,get_object_or_404 #loads HTML template with data and returns it as a web response
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  #its like @loginrequired decorator but for class based views, UserPassesTest only allows the logged in user to access their content for modification
from .models import Post # the dot before models is used as the models file is in the same directory(package)
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render (request,'blog/home.html',context) #parameters are requst (HTTP request sent by user's browser to build the response properly), template (the HTML file you want to display) path, context(Python dictionary that u want to send to the file, only a single dictionary)

class PostListView(ListView):
    model=Post #tells the class what model to query for the listview
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-date_posted'] #auto arranges the objects by date_posted in ascendiing order, for descending, put minus in front of date_posted
    paginate_by=5

class UserPostListView(ListView): #filtering the posts posted by a specific user
    model=Post #tells the class what model to query for the listview
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.author=self.request.user #overriding the submission to first pass the author name as current user name before submitting the form
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user #overriding the submission to first pass the author name as current user name before submitting the form
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object() #this gets the post that u are trying to update
        if self.request.user==post.author: #to check if the post author and logged in author are same to allow updates on posts
            return True
        return False
    
class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    success_url="/" #when the deletion is successful then where to direct the user is decided by this

    def test_func(self):
        post=self.get_object() #this gets the post that u are trying to update
        if self.request.user==post.author: #to check if the post author and logged in author are same to allow updates on posts
            return True
        return False
        


def about(request):
    return render (request,'blog/about.html',{'title':'About'})



 