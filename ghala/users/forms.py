
from django import forms
from .models import Farmer


class CreateFarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['phone_number', 'phone_number_2', 'full_names', 'location', 'is_broker', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Render password field as a password input
        }

