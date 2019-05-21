from django import forms
from multiselectfield import MultiSelectFormField

class EnquiryForm(forms.Form):
    name = forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Number'
            }
        )
    )
    email = forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )

    COURSES_CHOICES = (
        ('Py', 'Python'),
        ('Dj', 'Django'),
        ('API', 'REST API'),
        ('UI', 'UI')
    )
    courses = MultiSelectFormField(max_length=100, choices=COURSES_CHOICES)

    LOCATION_CHOICES = (
        ('Hyd', 'Hyderabad'),
        ('Bang', 'Bangalore'),
        ('Che', 'Chennai'),
        ('Pune', 'Pune')
    )
    locations = MultiSelectFormField(max_length=100, choices=LOCATION_CHOICES)

    SHIFT_CHOICES = (
        ('Morg', 'Morning'),
        ('Aftn', 'AfterNoon'),
        ('Evng', 'Evening'),
        ('Ngt', 'Night')
    )
    shifts = MultiSelectFormField(max_length=100,choices=SHIFT_CHOICES)

    GENDER_CHOISES = (
        ('M','Male'),
        ('F','Female')
    )
    gender = forms.ChoiceField( widget=forms.RadioSelect, choices=GENDER_CHOISES)

    y = range(1970,2020)
    batch_start_date = forms.DateField(widget=forms.SelectDateWidget(years=y))
