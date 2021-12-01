from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.views_helpers import look_user
from users.forms import NewUserForm, NewUserFormUser
from django.contrib.auth.forms import PasswordChangeForm #Pal password change

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

def register_request_user(request):
	if request.method == "POST":
		form = NewUserFormUser(request.POST)
		print(form)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserFormUser()
	return render (request=request, template_name="register_user.html", context={"register_form":form})

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
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("main:index")


# Modificar para nombres en register

#Funciones de prueba
def register_user(request):
	return render(request, "register_user.html")

def register_psicologo(request):
	return render(request, "register_psicologo.html")

def home_user(request):
	return render(request, "home.html")

def home_psicologo(request):
	return render(request, "home_psicologo.html")

def write_journal(request):
	return render(request, "journal.html")

def show_terms(request):
	return render(request, "terminos.html")

def show_privacy(request):
	return render(request, "privacidad.html")

def show_test(request):
	return render(request, "test.html")

def show_emociones(request):
	return render(request, "emociones.html")

def show_Login(request):
	return render(request,"Login.html")
	
# Agregar el cambio de password
def change_psswd(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request=request, template_name="change_psswd.html", context={"change_psswd":form})


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
