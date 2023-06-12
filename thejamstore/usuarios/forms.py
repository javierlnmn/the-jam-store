from django import forms
from django.contrib.auth.hashers import make_password
from usuarios.models import Custom_User, Categoria_Usuario


class RegistrarUsuarioForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria_Usuario.objects.all(), empty_label=None)

    class Meta:
        model = Custom_User
        fields = ['username', 'password', 'email', 'categoria']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class ActualizarUsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'first_name', 'last_name', 'telefono']