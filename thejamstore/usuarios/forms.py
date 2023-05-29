from django import forms
from django.contrib.auth.hashers import make_password
from usuarios.models import Custom_User


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Custom_User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user