from django import forms
from usuarios.models import Datos

class UsuariosForm(forms.ModelForm):
	class Meta:
		model = Datos