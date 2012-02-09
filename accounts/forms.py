from django import forms


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField( widget=forms.PasswordInput, label="Password" )
	email = forms.EmailField(required=False)