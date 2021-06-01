from django import forms  

from django.contrib.auth.models import User 

from .models import *
class ContactForm(forms.ModelForm): 
    class Meta : 
        model = Contact
        fields = ["name","email","message"] 
