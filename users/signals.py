from django.db.models.signals import post_save #a signal that gets triggered when an object is saved
from django.contrib.auth.models import User #this will be the signal sender
from django.dispatch import receiver
from .models import Profile

"""
This file is describing an event-driven connection between two models
Sender: User (where user is created)
Reciever: Profile (automatically responds to the sender)
Signal: post_save (the event gets fired when an object is saved by the sender)
Everytime a user is created or saved, automatically create or save its profile

The @receiver connects the signal to the custom function, when the post save signal is sent by user, it tells to run the function right below it

In the create function:
sender: which model sent the signal (here, the user)
instance: the actual object (the new user)
created: true when a new object is created, not updated
**kwargs: any extra data Django sends
"""

@receiver(post_save, sender=User) #parameters: signal, sender (when a user is saved, send post_save signal) which is received by the receiver decorator
def create_profile(sender,instance,created,**kwargs): #the receiver is the create_profile function
    if created:
        Profile.objects.create(user=instance)

"""
In below function, after the user already exists, this ensures that whenever the user is saved again (updating profile), the linked profile also gets saved, keeping them synced
"""
@receiver(post_save, sender=User) #parameters: signal, sender (when a user is saved, send post_save signal) which is received by the receiver decorator
def save_profile(sender,instance,created,**kwargs): #the receiver is the create_profile function
    instance.profile.save()
