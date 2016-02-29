from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout

loggedin 					= False
recent_login 			= False
recent_register 	= False
recent_logout 		= False
invalid_login 		= False
confirm_fail 			= False
name_fail 				= False
email_fail 				= False
email_in_use_fail	= False

def index(request):
	global recent_login
	global loggedin

	login = recent_login

	if recent_login:
		recent_login = False

	return render(request, 'index.html', {'recent_login' : login, 'loggedin' : loggedin})		

def media(request):
	global loggedin
	return render(request, 'media.html', {'loggedin' : loggedin})

def robots(request):
	global loggedin
	return render(request, 'robots.html', {'loggedin' : loggedin})

def aboutus(request):
	global loggedin
	return render(request, 'aboutus.html', {'loggedin' : loggedin})	

def sponsors(request):
	global loggedin
	return render(request, 'sponsors.html', {'loggedin' : loggedin})		

def login(request):
	global recent_register
	global loggedin
	global invalid_login
	global confirm_fail
	global name_fail
	global email_fail
	global email_in_use_fail

	register = recent_register
	invalid = invalid_login
	confirm = confirm_fail
	name = name_fail
	email = email_fail
	email_in_use = email_in_use_fail

	if recent_register:
		recent_register = False
	if invalid_login:
		invalid_login = False
	if confirm_fail:
		confirm_fail = False
	if name_fail:
		name_fail = False
	if email_fail:
		email_fail = False
	if email_in_use_fail:
		email_in_use_fail = False

	return render(request, 'login.html', {'recent_register' : register, 'loggedin' : loggedin,
																			  'invalid_login' : invalid, 'confirm_fail' : confirm,
																			  'email_fail' : email, 'name_fail' : name, 'email_in_use_fail' : email_in_use}) 

def authentication(request):
	global loggedin
	global recent_login
	global invalid_login
	email = request.POST.get('email', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=email, password=password)

	if user is not None:
		auth.login(request, user)
		loggedin = True
		recent_login = True
		return HttpResponseRedirect('/')
	else:
		loggedin = False
		recent_login = False
		invalid_login = True
		return HttpResponseRedirect('/login/')

def register(request):
	global recent_register
	global confirm_fail
	global name_fail
	global email_fail
	global email_in_use_fail

	name 			= request.POST.get('name', '')
	email 		= request.POST.get('email', '')
	phone			= request.POST.get('phone', '')
	password  = request.POST.get('password', '')
	confirm 	= request.POST.get('confirm', '')

	if password != '':
		if password != confirm:
			confirm_fail = True
	else:
		confirm_fail = True

	if name == '':
		name_fail = True

	if email == '':
		email_fail = True

	if User.objects.filter(username=email).exists():
		email_in_use_fail = True

	if confirm_fail | name_fail | email_fail | email_in_use_fail:
		return HttpResponseRedirect('/login/')

	user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
	recent_register = True
	return HttpResponseRedirect('/login/')

def logout_view(request):
	global loggedin
	global recent_logout
	logout(request)
	loggedin = False
	recent_logout = True
	return HttpResponseRedirect("/")
