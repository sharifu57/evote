from email import message
from multiprocessing import context
from typing import List
from django.views.generic.list import ListView
from pyexpat import model
from unicodedata import category
from django.shortcuts import render, redirect
from urllib import request
from django.views.generic import TemplateView
from voting.forms import CreateUserForm, LoginForm, NominationForm, VoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import constants as messages
from django_user_agents.utils import get_user_agent
from ipware import get_client_ip
# from django.contrib import messages
from django.db.models import Count
from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login

from voting.models import *

# Create your views here.
class HomePage(TemplateView):
    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)
        #client_addr = request.META.get('HTTP_X_FORWARDED_FOR')
        ipaddress= get_client_ip(request)
        #client_addr, is_routable = get_client_ip(request, request_header_order=['X_FORWARDED_FOR', 'REMOTE_ADDR'])


        print("+++++++", ipaddress)
        categories = Category.objects.all()

        categories.ipaddress = ipaddress;
        
        print("____ip add", categories.ipaddress)

        context = {'categories': categories}
        return render(request, 'links/home.html', context)


class NominationPage(TemplateView):
    def get(self, request, pk):

        getcategory = Category.objects.get(id=pk)
        nominations = Nomination.objects.filter(category_id=getcategory)
        
        context = {'nominations': nominations, 'category': getcategory}
        return render(request, 'links/nomination.html', context)




def submit_vote(request):

        ipaddress = get_client_ip(request)
       
        form = VoteForm()

        if request.method == 'POST':
            form = VoteForm(request.POST, ipaddress=ipaddress)

            if form.is_valid():
                form.save()

                messages.info(request, 'Your vote have been successfuly sent')

                messages.success = (request, 'you have already voted in this category '
                        f'{ipaddress}. Please choose another.')

                return redirect('home')
            else:
                form = VoteForm()

            context = {'form': form,}
            return render(request, 'links/home.html', context)
        return render(request, 'links/home.html')



# admin part
class AdminAuth(View):
    def get(self, request,  *args, **kwargs):

        context = {
            "title": " Login",
            "form": LoginForm(),
            "next": next,
        }

        return render(request, 'administrator/login.html', context)

    def post(self, request):
        form = LoginForm()
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('dashboard')
            else:
                form = LoginForm()
            
            context = {'form': form}
            return render(request, 'administrator/login/', context)
        else:
            return render(request, 'administrator/login/')



class Dashboard(TemplateView):
    def get(self, request):
        
        categories = Category.objects.all()
        count_categories =  categories.count()

        nominations = Nomination.objects.all()
        count_nominations =  nominations.count()

        votes = Vote.objects.all()
        count_votes = votes.count()
        
        latest_votes = Vote.objects.all().order_by('-id')[:5]

       
       
        context = {'categories': count_categories, 'nominations': count_nominations, 'votes': count_votes, 'voting': latest_votes}
        return render(request, 'administrator/dashboard.html', context)



# nominations
class CreateNominations(TemplateView):
    def get(self, request):

        categories = Category.objects.all()
        
        context = {'categories':categories}
        return render(request, 'nominees/addnomination.html', context)


    def post(self, request):

        form = NominationForm()


        if request.method == 'POST':
            form = NominationForm(request.POST)

            if form.is_valid():
                print("=====> success")
                form.save()
                messages.success(request, 'Account was created for ')
                return redirect('success')
            else:
                print("=======> failed")
        context = {'form': form}
        return render(request, 'nominees/addnomination.html', context)



def success(request):

    return render(request, 'nominees/success.html')