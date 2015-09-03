from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>Home Page</title><body>Nama : Gede Wahyu<br>NPM : 1206219073</body></html>')

# Create your views here.
