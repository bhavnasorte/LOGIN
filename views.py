from django.shortcuts import render, HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html') 



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        data=User.objects.get(email=email)
        if data.email == email:      
            auth.login(request,request.user)
            return redirect('index')


        else:
            print("enter correct credential")
            messages.info(request,"PLEASE !!!ENTER CORRECT USERNAME AND PASSWORD!!!")
            return redirect('/')


    else:        
        return render(request, 'login.html') 

def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username):
                messages.info(request,'EMAIL ID  IS ALREADY EXITS')
                print('USERNAME IS ALREADY EXITS')
                return redirect('registration')
            elif User.objects.filter(email=email):
                messages.info(request,'EMAIL ID  IS ALREADY EXITS')
                print('EMAIL ID  IS ALREADY EXITS')
                return redirect('registration')
            else:
                var=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                print("USER CREATED")
                var.save()
                messages.info(request,'REGISTRATION SUCCESSFULLY ! LOGIN NOW !')
                return HttpResponseRedirect("/")
        else:
            messages.info(request,'PASSWORD NOT MATCHED')
            return redirect('registration')
    else:
        return render(request,'registration.html')




#========================================================================================================================================================================
