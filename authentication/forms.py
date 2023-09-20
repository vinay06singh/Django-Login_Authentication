from django import forms
from .models import UserProfile

class HomeForm(forms.Form):
    message = forms.CharField(label='Enter a message', max_length=100)
    
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
