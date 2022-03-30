from dataclasses import fields
from urllib import request
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

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
