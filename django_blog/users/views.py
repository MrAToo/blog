from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


def registration(request):
    '''Регистрация пользователя'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                f'Ваш аккаунт создан! Теперь вы можете в него войти'
                )
            return redirect('login')
    else:    
        form = UserRegisterForm()
        
        
    return render(request, 'users/register.html', {'form':form})        


@login_required
def profile(request):
    '''Профиль пользователя'''
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,
                f'Ваш профиль успешно изменен'
                )
            return redirect('profile')                                         
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }

    return render(request, 'users/profile.html', context)
    '''testing'''