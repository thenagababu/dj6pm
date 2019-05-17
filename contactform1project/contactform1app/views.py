from django.shortcuts import render
from.models import Empdata
from .forms import Empform
from django.http.response import HttpResponse


def Contact_view(request):
    if request.method=="POST":


        eform=Empform(request.POST)
        if eform.is_valid():

            enamae = request.POST.get('ename', '')
            sal = request.POST.get('sal', '')
            email = request.POST.get('email', '')
            loc= request.POST.get('loc', '')
            data = Empdata(ename=enamae, sal=sal, email=email, loc=loc)
            data.save()
            eform = Empform()
            return render(request,'emp_home.html', {'abc':eform})
        else:
            return HttpResponse('invalid data')
    else:
        eform=Empform()
        return render(request ,'emp_home.html',{'abc':eform})

