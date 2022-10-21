from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }


class SigninFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget = forms.PasswordInput())

