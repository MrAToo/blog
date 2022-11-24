from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserRegisterForm(UserCreationForm):
    '''Форма регистрации'''
    email = forms.EmailField()


    class Meta:
        '''В этом классе находится то, с чем будет взаимодействовать форма выше'''
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    '''Форма изменения данных пользователя'''
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']      


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']        