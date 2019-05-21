from django.shortcuts import render

def main_page(request):
    return render(request,'base.html')


def home_page(request):
    return render(request,'home_page.html')

def contact_page(request):
    return render(request,'contact_page.html')

def courses_page(request):
    return render(request,'courses_page.html')

def feedback_page(request):
    return render(request,'feedback_page.html')

def ourteam_page(request):
    return render(request,'ourteam_page.html')

def gallery_page(request):
    return render(request,'gallery_page.html')
