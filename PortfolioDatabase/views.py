from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Portfolio
from django.template import loader

def Hobbies(request):
    hobby_list = Hobby.objects.all()
    context = {
        'hobby_list': hobby_list,
    }
    return render(request, 'portfolioDatabase/hobby_index.html', context)

def Home(request):
    return render(request, 'portfolioDatabase/home_index.html')

def Port(request):
    item_list = Portfolio.objects.all()
    context = {
        'item_list': item_list
    }
    return render(request, 'portfolioDatabase/item_index.html', context)


def Contact(request):
    return render(request, 'portfolioDatabase/contact_index.html')


def hobby_detail(request, hobby_id):
    hobby = Hobby.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby
    }
    return render(request, 'portfolioDatabase/hobby_detail.html', context)

def item_detail(request, item_id):
    item = Portfolio.objects.get(pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'portfolioDatabase/item_detail.html', context)