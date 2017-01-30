from django import forms
from crispy_forms.helper import FormHelper
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
    )
from django.http import HttpResponse
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=30, required=True, widget=forms.TextInput())
    password = forms.CharField(label="password", max_length=30, required=True, widget=forms.PasswordInput())

    def clean(self, *arg, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                return HttpResponse (forms.ValidationError("This user does not exist. Please check again."))

            elif not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            elif not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*arg, **kwargs)

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=self.cleaned_data.get('username')).count():
            raise forms.ValidationError("This username is already in use")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = self.cleaned_data.get('email')).count():
            raise forms.ValidationError("This email is already in use")
        return email




    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("The passwords do not match")

        return password






















