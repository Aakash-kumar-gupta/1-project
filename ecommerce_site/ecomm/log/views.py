from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.


#creating user sign_up form 
def sign_up(request):
    if request.method =="POST":
        su=SignUpForm(request.POST)
        if su.is_valid():
            messages.success(request,"You Have Successfully Created Your Account")
            su.save()  
            
    else:
        su=SignUpForm()
    return render(request,'html/user_signup.html',{'form':su})    
    
    
#Creating login form

def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
           su= AuthenticationForm(request= request , data=request.POST)   
           if su.is_valid():
              uname= su.cleaned_data['username']
              upass= su.cleaned_data['password'] 
            
              user= authenticate(username=uname,password=upass)
    
              if user is not None:
                  login(request,user)
                  return HttpResponseRedirect('/home/')
                
        else:
            su=AuthenticationForm()
        return render(request,'html/user_login.html',{'form':su})    
        
    else:
        return HttpResponseRedirect('/home/')              
        
        
#creating home page

def home1(request):
    if request.user.is_authenticated:
        return render(request,'html/home.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
    
    
# creating a logout func

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
    
    
# creating changepassword option
    
def changepass(request):
    if request.method== "POST":  
        su= PasswordChangeForm(request= request,data= request.POST)
        if su.is_valid():
            su.save