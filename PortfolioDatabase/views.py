from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby
from .models import Portfolio


def Home(request):
    return HttpResponse('Welcome to the site! I am Morgan, a 23 y/o student at Weber State in my last semester of my Computer Science degree.')

def Hobbies(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

def Portfolio(request):
    portfolio_list = Portfolio.objects.all()
    return HttpResponse(portfolio_list)

def Contact(request):
    return HttpResponse('morganmischo@mail.weber.edu')


