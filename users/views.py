from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.views_helpers import look_user
from users.forms import NewUserForm

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="index", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("main:index")

# Modificar para nombres en register
# Agregar el cambio de password
# Login con email en vez de username
"""
def login(request):
    email_user = request.GET["email"]
    password_user = request.GET["password"]
    user = authenticate(request, email = email_user, password = password_user)
    if user is not None:
        request.session['user_act'] = user.email
        context = {"user": user}
        login(request, user)
        return render(request, "index.html", context)
    else:
        return HttpResponse("El usuario no existe.")

def log_out(request):
    logout(request)
    del request.session['user_act']
    return render(request, "index.html")
"""