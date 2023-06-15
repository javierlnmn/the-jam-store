from django import forms
from django.contrib.auth.hashers import make_password
from usuarios.models import Custom_User, Categoria_Usuario, Direccion, Peticiones


class RegistrarUsuarioForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria_Usuario.objects.all(), empty_label=None, required=False)

    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password', 'categoria']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class ActualizarUsuarioForm(forms.ModelForm):
    foto_perfil = forms.ImageField(required=False)
    
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'first_name', 'last_name', 'telefono', 'foto_perfil']
        
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['provincia', 'municipio', 'cod_postal', 'calle', 'numero', 'piso', 'puerta', 'datos_adicionales']
        
class PeticionForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Peticiones
        fields = ['nombre_producto', 'precio', 'imagen', 'mensaje', 'talla']