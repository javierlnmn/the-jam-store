from django import forms
from usuarios.models import Custom_User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'password']