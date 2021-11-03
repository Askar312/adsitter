from django import forms
from .models import *
from django.contrib.auth.models import User

class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientsReview
        fields = ['name',
                  'image',
                  'review',
                  'user',]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control'}),
            'review' : forms.Textarea(attrs={'class':'form-control'}),
            'user' : forms.Select(attrs={'class':'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Имя'}),
            'email': forms.EmailInput(attrs={'class': 'email-bt', 'placeholder':'Емайл'}),
            'phone' : forms.TextInput(attrs={'class':'email-bt', 'placeholder':'Телефон'}),
            'message' : forms.Textarea(attrs={'class':'massage-bt', 'placeholder':'Сообщение', 'rows':'5'}),
        }
