from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def reg_view(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            first_name=request.post.get('first_name','')
            last_name=request.post.get('last_name','')
            username=request.post.get('username','')
            password=request.post.get('password','')
            email=request.post.get('email','')
            mobile=request.post.get('mobile','')

            data=RegistrationForm(
                 first_name=first_name,
                 last_name=last_name,
                 username=username,
                 password=password,
                 email=email,
                 mobile=mobile
              )
            data.save()
            lform=LoginForm()
            return render(request,'login_form.html',{'lform:lform'})
        else:
         return HttpResponse("invalid data")
    else:
        rform=RegistrationForm()
        return render(request,'reg_form.html',{'rform':rform})

def login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.post)
        if lform.is_valid():
            uname = request.post.get('username', '')
            pwd = request.post.get('password', '')
            uname1 = RegistrationData.objects.filter(username=uname)
            pwd1 = RegistrationData.objects.filter(password=pwd)

            if uname1 and pwd1:
                return HttpResponse("correct username and password")
            else:
                return HttpResponse("wrong username and password")


        else:
          return  HttpResponse("invalid data")
    else:
     lform=LoginForm()
     return render(request,'login_form.html',{'lfrom':lform})

