from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Portfolio
from django.template import loader

def Hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolioDatabase/index.html', context)

def Home(request):
    hobby_list = Hobby.objects.all()
    return HttpResponse(hobby_list)

def Portfolio(request):
    item_list = Portfolio.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'portfolioDatabase/index2.html', context)


def Contact(request):
    return HttpResponse('morganmischo@mail.weber.edu')


def detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'portfolioDatabase/detail.html', context)

def detail2(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'portfolioDatabase/detail2.html', context)