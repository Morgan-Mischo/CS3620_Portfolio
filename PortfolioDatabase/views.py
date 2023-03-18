from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby, Portfolio
from .forms import ItemForm
from .forms import ContactForm
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
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('contact')

    return render(request, 'portfolioDatabase/contact_index.html', {'form': form})


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

# def item_index(request):
#     return render(request, 'portfolioDatabase/item_index.html')

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio')

    return render(request, 'portfolioDatabase/item-form.html', {'form': form})

def update_item(request, id):
    item = Portfolio.objects.get(id=id)
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('portfolio')

    return render(request, 'portfolioDatabase/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Portfolio.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('portfolio')

    return render(request, 'portfolioDatabase/item-delete.html', {'item': item})

# def create_contact(request):
#     form = ContactForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('contact')
#
#     return render(request, 'portfolioDatabase/contact_index.html', {'form': form})