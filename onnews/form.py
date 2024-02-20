from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import blogs

class add_Editor(UserCreationForm):
    password1=forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(max_length=25,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
        'first_name': 'Name',
        'email': 'Gmail address' 
        }

    def clean_first_name(self):
        valname=self.cleaned_data['first_name']
        if not valname.replace(" ",'').isalpha():
            raise forms.ValidationError('Name should not contain number or special character')
        return valname.strip()
    

class update_Editor(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','email']
    
    def clean_first_name(self):
        valname=self.cleaned_data['first_name']
        if not valname.replace(" ",'').isalpha():
            raise forms.ValidationError('Name should not contain number or special character')
        return valname.strip()
    
   

class Loginform(AuthenticationForm):
     username = forms.CharField(label='Username')
     class Meta:
         fields="__all__"

class blog_add(forms.ModelForm):
    title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model=blogs
        fields="__all__"
