from allauth.account.forms import LoginForm,SignupForm
from django import forms
from django.core.exceptions import ValidationError


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border text-black rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username or Email'
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 text-black border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize fields
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Email Address'
        })
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })


    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one numeric character.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one alphabetic character.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
            raise ValidationError("Password must contain at least one special character.")
        
        return password