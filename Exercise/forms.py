from django import forms
from .models import name,gender,dob,height,weight,email

class nameform(forms.ModelForm):
    class Meta:
        model=name
        fields ='__all__'


class genderform(forms.ModelForm):
    class Meta:
        model=gender
        fields ='__all__'

class ageform(forms.ModelForm):
    class Meta:
        model=dob
        fields ='__all__'

class heightform(forms.ModelForm):
    class Meta:
        model=height
        fields ='__all__'

class weightform(forms.ModelForm):
    class Meta:
        model=weight
        fields ='__all__'

class emailform(forms.ModelForm):
    class Meta:
        model=email
        fields ='__all__'