from django import forms

class Empform(forms.Form):
    ename=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'your name',
                'class':'form-control'
            }
        )
    )

    sal=forms.IntegerField(
            label="Enter your salary",
            widget=forms.NumberInput(
                    attrs={
                        'placeholder':'your salary',
                        'class':'form-control'
                    }
            )
    )
    email=forms.EmailField(
            label="Enter your email",
            widget=forms.EmailInput(
                    attrs={
                        'placeholder':'your Email',
                        'class':'form-control'
                    }
            )
    )
    loc=forms.CharField(
            label='Enter your location',
            widget=forms.TextInput(
                    attrs={
                        'placeholder':'your location',
                        'class':'form-control'
                    }
            )
    )
