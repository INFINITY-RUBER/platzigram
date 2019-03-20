""" User Forms """

#Django
from django import forms


#Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """ Sign up  forms"""
    
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput())
    password_confirmation = forms.CharField(
        max_length=70, 
        widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6, 
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        username_token = User.objects.filter(username=username).exists() # valida si hay un usuario con repetido, retorna un booleano
        if username_token:
            raise forms.ValidationError('username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
 
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

   

class ProfileForm(forms.Form):
    """ Profile forms """

    website = forms.URLField(max_length=2000, required=True) 
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
