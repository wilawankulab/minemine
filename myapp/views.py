from django.shortcuts import render
from django.utils import encoding #smart_unicode
from urllib.parse import parse_qsl

from .models import Service

# Create your views here.
def services(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/services.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/services.html', { 'services': services })

def home(req):
    return render(req, 'myapp/home.html')
def about(req):
    return render(req, 'myapp/about.html')

def photos(req):
    return render(req, 'myapp/photos.html')

def contact(req):
    return render(req, 'myapp/contact.html')

