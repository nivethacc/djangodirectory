from django import forms

from .models import RegistrationModels

class RegistrationCreateForm(forms.ModelForm):
	class Meta:
		model = RegistrationModels
		fields = [
		'recruiter_name',
		'company',
		'email',	
		]