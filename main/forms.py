from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder':'Email'}),
            'phone' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Phone'}),
            'message' : forms.Textarea(attrs={'class':'massage-bt', 'placeholder':'Massage', 'rows':'5'}),
        }
