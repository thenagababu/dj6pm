from django import forms

class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label='enter first name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'first name',
                'class':'form-control'
            }
        )
    )
    last_name=forms.CharField(
        label='enter last name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'last name',
                'class':'form-control'
            }
        )
    )
    mobile=forms.IntegerField(
        label=' enter mobile number',
        widget=forms.NumberInput(
            attrs={
                'placeholder':'mobile number',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label=' enter your email',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'email',
                'class':'form-control'
            }
        )
    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='enter user name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='enter password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )
