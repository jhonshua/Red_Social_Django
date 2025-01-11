from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile

# Hereda de UserCreationForm una clase de Django que proporciona una base sólida para formularios de registro de usuarios
class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'username', 'email', 'password1', 'password2']


#Hereda de forms.ModelForm esta clase es ideal para crear formularios basados en modelos de Django
class PostForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
								'id':'contentsBox', 'rows':'3',
								'placeholder':'¿Qué está pasando?'}))

	class Meta:
		model = Post
		fields = ['content']
  
# UserUpdateForm: Se utiliza para permitir a los usuarios editar su información básica, como el nombre y el nombre de usuario.

# ProfileUpdateForm: Se utiliza para permitir a los usuarios editar información más específica de su perfil, como una imagen de perfil y una biografía.

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'username']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'bio']


