from urllib import request
from wsgiref.validate import validator
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.core.validators import EmailValidator
from django.db.models import Q
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        self.ipaddress = kwargs.pop("ipaddress", None)
        super(VoteForm, self).__init__(*args, **kwargs)


    def save(self, *args, **kwargs):
        form = super(VoteForm, self).save(*args, **kwargs, commit=False)
        form.ipaddress = self.ipaddress
        if(not Vote.objects.filter(category_id=self.cleaned_data.get("category"), ipaddress=self.ipaddress).exists()):
            form.save()
        return form


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class NominationForm(ModelForm):
    class Meta:
        model = Nomination
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


    def clean(self):
        username = str(self.cleaned_data.get('username')).strip().replace(" ", "").lower()
        password = str(self.cleaned_data.get('password')).strip().replace(" ", "")
        validator = EmailValidator()
        try:
            validator(username)
        except:
            pass
           
        if User.objects.filter(Q(username=username)| Q(email=username)).exists():
            user_obj = User.objects.filter(Q(username=username) | Q(email=username)).first()
            user = authenticate(username=user_obj.username, password=password)
        else:
            raise forms.ValidationError("Sorry, that Login Failed")
        if User.objects.filter(Q(username=username)| Q(email=username)).exists():
            if not user or not user.is_active:
                self._errors['password'] = "Invalid Password"
        else:
            self._errors['username'] = f"{self.cleaned_data.get('username')} Invalid"

        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that Login Failed")
        return self.cleaned_data

    def login(self):
        user = None
        username = str(self.cleaned_data.get('username')).strip().replace(" ", "").lower()
        password = str(self.cleaned_data.get('password')).strip()
        validator = EmailValidator()
        try:
            validator(username)
        except:
            pass
        
        if User.objects.filter(Q(username=str(username).lower())| Q(email=str(username).lower())).exists():
            user_obj = User.objects.filter(Q(username=str(username).lower()) | Q(email=str(username).lower())).first()
            user = authenticate(username=user_obj.username, password=password)
        else:
            return None
        return user

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)