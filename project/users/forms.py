from django import forms

class ProfileRegForm(forms.Form):
    username = forms.CharField(
        max_length=128,
    )
    email = forms.EmailField(
        max_length=128,
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput()
    )
    password_again = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput()
    )

class ProfileLoginForm(forms.Form):
    username = forms.CharField(
        max_length=128
    )
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput()
    )