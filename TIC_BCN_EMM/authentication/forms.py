from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom usuari"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contrasenya"
    )
    
class LoginForm(forms.Form):
    username = forms.CharField(
        label="Nom usuari"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contrasenya"
    )