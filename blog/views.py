<<<<<<< HEAD
from django.shortcuts import render

def home(request):
	return render(request, 'index.html');

def about(request):
	return render(request, 'about.html');
=======
from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	# return HttpResponse("About Page");
	return render(request, 'about.html');

def home(request):
	# return HttpResponse("Home Page");
	return render(request, 'index.html');
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
