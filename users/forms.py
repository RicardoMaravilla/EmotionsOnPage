from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from users.models import entrada_user, psicologos_user, usuarios_user


# Create your forms here.
"""
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NewUserFormUser(UserCreationForm):
	required_css_class = 'required'
	username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_ characters."})
	email = forms.EmailField(label="E-mail")
	password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
	password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")

	def clean_username(self):            
		existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError("A user with that username already exists.")
		else:
			return self.cleaned_data['username']

	def clean_email(self):
        #if you want unique email address. else delete this function
		if User.objects.filter(email__iexact=self.cleaned_data['email']):
			raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
		return self.cleaned_data['email']

	def clean(self):            
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError("The two password fields didn't match.")
		return self.cleaned_data
"""
class NewPsicologoForm(ModelForm):
	class Meta:
		model = psicologos_user
		fields = ('nombre', 'apellido', 'email', 'telefono', 'titulo', 'consultorio', 'especialidad', 'password')
	
	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefono', 'size': '10'}))
	titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo', 'size': '50'},))
	consultorio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Consultorio', 'size': '50'}))
	especialidad = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Especialidad' ,'size': '100'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class NewUsuarioForm(ModelForm):
	class Meta:
		model = usuarios_user
		fields = ('nombre', 'apellido', 'email', 'telefono', 'problema', 'direccion', 'password')

	nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	telefono = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Telefono', 'size': '10'}))
	problema = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Titulo', 'size': '50'},))
	direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Consultorio', 'size': '50'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	
class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
