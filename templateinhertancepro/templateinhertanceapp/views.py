from django.shortcuts import render

def base_home_view(request):
    return render(request,'base.html')

def home_home_view(request):
    return render(request,'base_home.html')

def home_contact_view(request):
    return render(request,'base_contact.html')

def home_services_view(request):
    return render(request,'base_services.html')

def home_feedback_view(request):
    return render(request,'base_feedback.html')
