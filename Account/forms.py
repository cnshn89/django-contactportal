from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60)

    class Meta:
        model=Account
        fields=("email","username","first_last_name","department","password1","password2")


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=60,label="Parola",widget=forms.PasswordInput())

    class Meta:
        model=Account
        fields=("email","password")

    def clean(self):
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']

        if not authenticate(email=email,password=password):
            raise forms.ValidationError("Email adresi veya parola hatalı !")


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model=Account
        fields=("email","username","first_last_name","department")

    def clean_email(self): #Girilen email adresi sistemde var mı ?
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('"%s" Email adresi sistemde mevcut.' % account.email)


    def clean_username(self): #Girilen kullanıcı adı sistemde var mı ?
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account=Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('"%s" kullanıcı adı sistemde mevcut.' % account.username)        
