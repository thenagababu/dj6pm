from django.shortcuts import render
from .models import EnquiryData
from .forms import EnquiryForm

def enquiry_view(request):
    if request.method == "POST":
        eform = EnquiryForm(request.POST)
        if eform.is_valid():
            name = request.POST.get('name','')
            mobile = request.POST.get('mobile','')
            email = request.POST.get('email','')
            courses = eform.cleaned_data.get('courses','')
            locations = eform.cleaned_data.get('locations','')
            shifts = eform.cleaned_data.get('shifts','')
            gender = eform.cleaned_data.get('gender','')
            batch_start_date = eform.cleaned_data.get('batch_start_date','')

            data = EnquiryData(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                locations=locations,
                shifts=shifts,
                gender=gender,
                batch_start_date=batch_start_date
            )
            data.save()
            eform = EnquiryForm()
            return render(request,'enquiry.html',{'eform':eform})
    else:
        eform = EnquiryForm()
        return render(request,'enquiry.html',{'eform':eform})
