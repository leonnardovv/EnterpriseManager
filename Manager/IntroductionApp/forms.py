from django import forms


class RegisterForm(forms.Form):
    userName = forms.CharField(label="Username",widget=forms.TextInput(attrs={'placeholder': 'username'}))
    firstName = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'placeholder': 'Prenume'}))
    lastName = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'placeholder': 'Nume'}))
    passWord = forms.CharField(label="Password", widget=forms.PasswordInput)
    birthDay = forms.DateField(label="Birth Day", input_formats=['%d-%m-%Y'],widget=forms.TextInput(attrs={'placeholder': 'Day-Mon-Year'}))


class LoginForm(forms.Form):
    email = forms.CharField(label="email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
