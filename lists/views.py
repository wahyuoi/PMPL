from django.core.exceptions import ValidationError
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
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/lists/%d/' % (list_.id,))

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
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % (list_.id))
