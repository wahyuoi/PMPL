from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']  #1
        Item.objects.create(text=new_item_text)  #2
        return redirect('/')
    else:
        new_item_text = ''  #3
    items = Item.objects.all()        
    if items.count() == 0:
        comment = "yey, waktunya berlibur"
    elif items.count() < 5:
        comment = "sibuk tapi santai"
    else:
        comment = "oh tidak"
    return render(request, 'home.html', {
        'items': items,  #4
        'comment' : comment,
    })
