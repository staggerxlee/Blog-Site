from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title =models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User,on_delete=models.CASCADE) #what cascade does is when you delete the user, it deletes all its relative data, posts and etc.

    def __str__(self): #self is the current object that you are accessing right now, like if your accessing post 1, then self=post 1 object
        return self.title #returns the title of the currenly accessed object's title
  