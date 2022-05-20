# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 05:11:06 2019

@author: 10957
"""

'''

from django import forms
from django.contrib.auth.models import User

class RegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')
        #widgets = {'intro': forms.Textarea(attrs={'cols': 80})}
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)



class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)

    
    
'''
        
    