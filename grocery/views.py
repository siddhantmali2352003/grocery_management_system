from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from groceryproducts.models import category

def SignUpPage(request):
    status=''
    status1=''
    if request.method == "POST":
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')

        status1="Password doesn't match!!"


        if pass1!=pass2:
            return render(request,"signup.html",{'status1':status1})
        else:
            try:
                existing_user = User.objects.get(email=email)
                status="<p style='color:red';>User already exists!! Please Sign in</p>"
            except User.DoesNotExist:    
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.save()
                status="<p style='color:green';>Your Account has been created successfully! &#128512;</p>"
            
    return render(request,"signup.html",{'status':status})

def LoginPage(request):
    status2=''
    if request.method == "POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username, password=pass1)

        status2="Username or Password is incorrect"

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,"login.html",{'status2':status2})
        
    return render(request,"login.html")

@login_required(login_url="/login/")
def home(request):
    categories = category.objects.all()
    if request.user.is_superuser:
        message = "Welcome Admin!"
    else:
        message = "Welcome " + request.user.username + "!"
        
    context = {
        'categories': categories,
        'message': message
    }
    
    return render(request, "home.html", context)


def LogoutPage(request):
    logout(request)
    return redirect('login')
