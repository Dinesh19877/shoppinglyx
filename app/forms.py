from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import customer

class CustomerRegister(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {"email": "Email"}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control" }))
    password = forms.CharField(label=_('Password'),  strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control','autocomplete':'current-password'}))
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_('Old Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autofocus': True, 'autocomplete': 'current-password'})
    )
    new_password1 = forms.CharField(
        label=_('New Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html()
    )
    new_password2 = forms.CharField(
        label=_('Confirm New Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'})
    )
    
    
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ['name','localtiy','city','zipcode','state']
        
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'localtiy': forms.TextInput(attrs={'class': 'form-control'}),
        'city': forms.TextInput(attrs={'class': 'form-control'}),
        'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        'state': forms.Select(attrs={'class': 'form-control'}),
        
}   
