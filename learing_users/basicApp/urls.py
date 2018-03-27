from django.urls import path
from basicApp import views

#Template url
app_name='app'


urlpatterns = [
    path('register',views.register,name='register'),
    path('login_user',views.login_user,name='login_user'),

]
