from django.http import HttpResponse
from django.shortcuts import render, redirect
from lists.models import Item, List

def home_page(request):
    list_ = List.objects.create()
    items = Item.objects.filter(list=list_)
    cnt = items.count() 
    if (cnt==0):
        comment = "yey, waktunya berlibur"
    elif (cnt<5):
        comment = "sibuk tapi santai"
    else :
        comment = "oh tidak"
    return render(request, 'home.html', {'comment':comment})
def blog_view(request):
    return render(request, 'blog.html', {'title' : 'Blog Gede'})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list_)
    cnt = items.count() 
    if (cnt==0):
        comment = "yey, waktunya berlibur"
    elif (cnt<5):
        comment = "sibuk tapi santai"
    else :
        comment = "oh tidak"
    return render(request, 'list.html', {'list':list_, 'comment':comment})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id))

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id))
