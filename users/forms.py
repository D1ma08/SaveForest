from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':  'text input form-control', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'regs input form-control', 'placeholder': 'Введите email'}),
            'password': forms.PasswordInput(attrs={'class': ' pass input form-control', 'placeholder': 'Введите пароль'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'text input form-control', 'placeholder': 'Введите имя'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'pass input form-control', 'placeholder': 'Введите пароль'})
    )