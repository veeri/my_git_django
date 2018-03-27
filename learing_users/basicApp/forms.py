from  django import forms
from django.contrib.auth.models import User
from basicApp.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #portfolio = forms.URLField(required=False)
    #picture=forms.ImageField(required=False)

     # user model has some attribute we are using thses model attribute for model
    #username,email,password and first_name are user model attribute
    class Meta():
        model=User
        fields=('username','email','password','first_name')


class UserProfileInfo(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('profile_site','profile_pic')
