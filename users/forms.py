from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError('Passwords are not saved.')
