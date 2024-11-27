from django import forms
from .models import Profile, Address


class ProfileForm(forms.ModelForm):   
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'profile_image', 'DOB', 'gender', 'mobile_number1', 'mobile_number2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Enter your first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Enter your first name',
            }),
            'email': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Enter your first name',
            }),
            'mobile_number1': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Enter your first name',
            }),
            'mobile_number2': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Enter your first name',
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'block text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none',
            }),
            'DOB': forms.DateInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'type': 'date',
            })
        }
        
        
class AddressForm(forms.ModelForm):   
    class Meta:
        model = Address
        fields = ['type', 'address', 'city', 'state', 'pincode']
        widgets = {
            'address': forms.Textarea(attrs={
                'class': 'p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Address',
                'style': 'height: 60px;'
            }),
            'city': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'City',
            }),
            'state': forms.TextInput(attrs={
                'class': ' p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'State',
            }),
            'pincode': forms.NumberInput(attrs={
                'class': 'h-12 p-2 border border-gray-300 rounded-md focus:ring-teal-500 focus:border-teal-500',
                'placeholder': 'Pin code',
            }),
            
        }