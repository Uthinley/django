from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
	return render(request,'index2.html')

def display_laptop(request):
	items = Laptop.objects.all()
	context = {
		'items': items,
		'header': 'Laptops'
	}

	return render(request,'index2.html',context)

def display_desktop(request):
	items = Desktop.objects.all()
	context = {
		'items': items,
		'header': 'Desktops'
	}

	return render(request,'index2.html',context)

def display_mobile(request):
	items = Mobile.objects.all()
	context = {
		'items': items,
		'header':'Mobiles'
	}

	return render(request,'index2.html',context)

def add_device(request,cls):
	if request.method == "POST":
		form = cls(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = cls()
		return render(request,'add_new.html',{'form': form})

def add_laptop(request):
	return add_device(request,LaptopForm)

def add_desktop(request):
	return add_device(request,DesktopForm)

def add_mobile(request):
	return add_device(request,MobileForm)

def home(request):
    try:
        response = request.GET['http://freegeoip.net/json/']
        geodata = response.json()
    except KeyError:
        response="error"
	return  render(request,'home.html',{
		'ip':geodata['ip'],
		'country':geodata['country_name']
	})
