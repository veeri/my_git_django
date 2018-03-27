from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    #create relationship (don't inherit from user!)
    # to add more attribute with first,last name we use OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #it will allow you to Add any Additonal attributes you want
    profile_site=models.URLField(blank=True)# blank=True because user have to fill
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)#user uploaded pics will be stored in profile_pics this foalder

    def __str__(self):
        #Built-in attribute of django.contrib.auth.models.User
        return self.user.username
