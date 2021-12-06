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
	if usuario:
		user = usuarios_user.objects.get(email=usuario)
		entradas = entrada_user.objects.filter(username=user)
		entradas_128525 = entradas.filter(emoji = '😍').count()
		entradas_128513 = entradas.filter(emoji = '😁').count()
		entradas_128528 = entradas.filter(emoji = '😐').count()
		entradas_128545 = entradas.filter(emoji = '😡').count()
		entradas_128546 = entradas.filter(emoji = '😢').count()

		cantidad_entradas = entradas.count()
		val_total_entradas = (entradas_128525*50) + (entradas_128513*30) + (entradas_128528*-5) + (entradas_128545*-10) + (entradas_128546*-15)

		if(val_total_entradas > 50):
			resultado_entradas =  'regular'
		elif(val_total_entradas > 20 and val_total_entradas <= 50):
			resultado_entradas =  'advertencia'
		else:
			resultado_entradas =  'peligro'

		print(resultado_entradas)

		context = {
			'tipo_usuario': tipo_usuario,
			'usuario': usuario,
			'entradas': entradas,
			'entradas_128525': entradas_128525,
			'entradas_128513': entradas_128513,
			'entradas_128528': entradas_128528,
			'entradas_128545': entradas_128545,
			'entradas_128546': entradas_128546,
			'resultado_entradas': resultado_entradas,
			'cantidad_entradas': cantidad_entradas,
		}
		return render(request, "home.html", context=context)

	return render(request, "home.html")

def home_psicologo(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	if usuario:
		psicologo = usuarios_user.objects.get(email=usuario)
		context = {
			'tipo_usuario': tipo_usuario,
			'usuario': usuario,
		}
		return render(request, "home_psicologo.html", context=context)
	return render(request, "home_psicologo.html")

def write_journal(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}

	if request.method == "POST":
		fecha = request.POST.get("j_date")
		emoji = request.POST.get("j_emotion")
		contenido = request.POST.get("j_entrada")
		user = usuarios_user.objects.get(email=usuario)
		
		new_entrada = entrada_user(fecha=fecha, emoji=emoji, contenido=contenido, username=user)
		new_entrada.save()
		return redirect("home_user")

	return render(request, "journal.html", context=context)

def show_terms(request):
	return render(request, "terminos.html")

def show_privacy(request):
	return render(request, "privacidad.html")

def show_test(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}

	return render(request, "test.html", context=context)

def show_test_result(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')

	if request.method == "POST":
		face = request.POST.get("face")
		dolor = request.POST.get("dolor")
		cancion = request.POST.get("cancion")

		if(face == 'in-love' and dolor=='in-love' and cancion == 'in-love'):
			resultado = 'in-love'
		if(face == 'angry' and dolor=='angry' and cancion == 'angry'):
			resultado = 'angry'
		if(face == 'happy' and dolor=='happy' and cancion == 'happy'):
			resultado = 'happy'
		if(face == 'sad' and dolor=='sad' and cancion == 'sad'):
			resultado = 'sad'
		if(face == 'neutral' and dolor=='neutral' and cancion == 'neutral'):
			resultado = 'neutral'
		else:
			resultado = 'neutral'
		context = {
			'tipo_usuario': tipo_usuario,
			'usuario': usuario,
			'resultado': resultado,
		}
	return render(request, "resultado_test.html", context=context)

def show_emociones(request):
	return render(request, "emociones.html")

def show_Login(request):
	return render(request,"Login.html")

def show_recomendaciones(request): 
	return render(request,"recomendaciones.html") 

def show_wikis(request): 
	return render(request,"wikis.html") 

def show_chat(request): 
	return render(request,"chat.html") 

def show_chat_psicologo(request): 
	return render(request,"chat_psicologo.html") 
	
# Agregar el cambio de password
def change_psswd(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}

	if request.method == "POST":
		old_password = request.POST.get("old_password")
		password1 = request.POST.get("new_password1")
		password2 = request.POST.get("new_password2")
		user = usuarios_user.objects.get(email=usuario)
		if(old_password == user.password):
			if(password1 == password2):
				user.password = password1
				user.save()
				return redirect("home_user")
		else:
			messages.error(request, "The old password is incorrect.")

	return render(request, "change_psswd.html", context=context)

def change_mail(request):
	tipo_usuario = request.session.get('tipo_usuario')
	usuario = request.session.get('usuario')
	context = {
		'tipo_usuario': tipo_usuario,
		'usuario': usuario,
	}

	if request.method == "POST":
		old_mail = request.POST.get("old_mail")
		mail1 = request.POST.get("new_mail1")
		mail2 = request.POST.get("new_mail2")
		user = usuarios_user.objects.get(email=usuario)
		if(old_mail == user.email):
			if(mail1 == mail2):
				user.email = mail1
				user.save()
				return redirect("home_user")
		else:
			messages.error(request, "The old mail is incorrect.")

	return render(request, "change_mail.html", context=context)

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
