from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
	return render(request, 'index.html')		

def media(request):
	return render(request, 'media.html')

def robots(request):
	return render(request, 'robots.html')

def aboutus(request):
	return render(request, 'aboutus.html')	

def sponsors(request):
	return render(request, 'sponsors.html')		