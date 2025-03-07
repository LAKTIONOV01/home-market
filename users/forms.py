from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'placeholder': 'Введите ваше имя пользователя',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'autofocus': True,
        'class': 'form-control',
        'placeholder': 'Введите ваш пароль',
    }))

    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserChangesForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control mt-3',
    }), required=False)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'readonly': True
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'readonly': True,
    }))

    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'username', 'email')

