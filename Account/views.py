from django.shortcuts import render, redirect, get_object_or_404
from Account.forms import RegistrationForm, LoginForm, AccountUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url="Account:login") 
def registerV(request): # Register User

    form = RegistrationForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email='email', password=raw_password)
        login(request, user)
        messages.success(request, "Kullanıcı oluşturuldu.")
        return redirect("index")

    return render(request, 'register.html', context)


def loginV(request): # Login User

    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, "Giriş yapıldı.")
                return redirect("index")
    else:
        form = LoginForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)


@login_required(login_url="Account:login")
def updateV(request): # Update User 
    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Güncelleme başarılı.")
            return redirect("index")
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "first_last_name": request.user.first_last_name,
                "department": request.user.department,
            }
        )

    context = {
        "form": form,
    }

    return render(request, "update.html", context)


def logoutV(request):
    logout(request)
    return redirect("index")



def passwordChangeV(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Şifre değiştirildi.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })