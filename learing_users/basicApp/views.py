from django.shortcuts import render
from basicApp.forms import UserForm,UserProfileInfo


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls  import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered=False

    if request.method == 'POST':
        User_Form=UserForm(data=request.POST)
        profile_Form=UserProfileInfo(data=request.POST)

        if User_Form.is_valid() and profile_Form.is_valid():
            user=User_Form.save()
            user.set_password(user.password)
            user.save()

            profile= profile_Form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered =True
        else:
            print(User_Form.errors,profile_Form.errors)

    else:
        User_Form=UserForm()
        profile_Form=UserProfileInfo()

    return render(request,'basic_app/registration.html',
                                {'user_form':User_Form,
                                 'profile_form':profile_Form,
                                 'registered':registered})

def login_user(request):

    if request.method=='POST':
        username=request.POST.get('input_username')
        password=request.POST.get('input_password')

        user=authenticate(username=username,password=password)# django will check the valid UserName and password internally with single line

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not Active')
        else:
            print("some one tried to login and failed!")
            print("Username:{} and password {}".format(username,password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'basic_app/login.html',{})

@login_required # make sure that only logging in user can only logout ..to do that we use decorators @login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("you have logged nice")
