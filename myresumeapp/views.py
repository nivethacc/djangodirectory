from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import RegistrationCreateForm
from .models import RegistrationModels

# Create your views here.

class HomeView(View):
	def get(self,request,*args,**kwargs):
		context={}
		return render(request,"base.html",context)

class RegistrationFormView(CreateView):
	form_class = RegistrationCreateForm
	template_name = 'forms.html'
	success_url ='/home/'

