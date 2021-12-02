from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import EmailValidator
from django.contrib.auth.models import User
from users.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from users.views_helpers import look_user
from users.forms import NewPsicologoForm, NewUsuarioForm, LoginForm
from django.contrib.auth.forms import PasswordChangeForm #Pal password change

# Create your views here.

"""
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
	return render(request=request, template_name="login.html", context={"login_form":form})
"""

def register_request_user(request):
	if request.method == "POST":
		form = NewUsuarioForm(request.POST)
		if form.is_valid():
			user = form.save()
			login_request(request)
			messages.success(request, "Registration successful." )
			return redirect("home_user")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUsuarioForm()
	return render (request=request, template_name="register_user.html", context={"register_form":form})

def register_request_psicologo(request):
	if request.method == "POST":
		form = NewPsicologoForm(request.POST)
		if form.is_valid():
			user = form.save()
			login_request(request)
			messages.success(request, "Registration successful." )
			return redirect("home_psicologo")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewPsicologoForm()
	return render (request=request, template_name="register_psicologo.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = psicologos_user.objects.filter(email=email, password=password)
			if user:
				#response = HttpResponse("Setting Cookie")
				#response.set_cookie('usuario', email)
				#response.set_cookie('tipo_usuario', 'psicologo')
				request.session['usuario'] = email
				request.session['tipo_usuario'] = 'psicologo'
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("home_psicologo")
			else:
				user = usuarios_user.objects.filter(email=email, password=password)
			if user:
				#response = HttpResponse("Setting Cookie")
				#response.set_cookie('usuario', email)
				#response.set_cookie('tipo_usuario', 'usuario')
				request.session['usuario'] = email
				request.session['tipo_usuario'] = 'usuario'
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("home_user")
			else:
				messages.error(request,"Invalid username or password.")
	form = LoginForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	response = HttpResponse("Setting Cookie")
	response.delete_cookie('usuario')
	response.delete_cookie('tipo_usuario')
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("index")


# Modificar para nombres en register

#Funciones de prueba

def home(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}
	if(tipo_usuario == 'psicologo'):
		return render(request, "home_psicologo.html", context=context)
	return render(request, "home_user.html", context=context)

def home_user(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}
	return render(request, "home.html", context=context)

def home_psicologo(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}
	return render(request, "home_psicologo.html")

def write_journal(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}

	if request.method == "POST":
		date = request.POST.get("j_date")
		emotion = request.POST.get("j_emotion")
		entrada = request.POST.get("j_entrada")
		user = usuarios_user.objects.get(email=usuario)
		print(user.nombre)

	return render(request, "journal.html", context=context)

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

def show_recomendaciones(request): 
	return render(request,"recomendaciones.html") 

def show_wikis(request): 
	return render(request,"wikis.html") 
	
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
