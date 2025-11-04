from django.db import models # Django's base model class (for creating database tables)
from django.contrib.auth.models import User #Django's built-in User model (the one that stores username, email, password, etc.)
from PIL import Image

class Profile(models.Model): # Create a Profile model that extends the existing User model (inheritance)
    user=models.OneToOneField(User, on_delete=models.CASCADE)  # Creating a one-to-one relationship with the User model
    image=models.ImageField(default='default.jpg',upload_to="profile_picture") # Add an image field for profile pictures
    
    def __str__(self):  # Define what the object should look like when printed or displayed in the admin panel,  Instead of showing <Profile: Profile object (1)>, it will show something like "saswat Profile"
        return f'{self.user.username} Profile'

    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        
        img=Image.open(self.image.path)
        if img.height>300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    
