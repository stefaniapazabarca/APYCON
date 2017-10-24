from django.shortcuts import render
import ipdb
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.forms import ModelForm
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SpeakerRegisterForm

@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
	
	def get(self, request):
		#print(request)
		#ipdb.set_trace()
		#creo una instancia del modelo User y le pongo valores a sus atributos
		pass
	
	def post(self, request):
		user = SpeakerRegisterForm(request.POST)
		if user.is_valid():
			user.save()
			return JsonResponse({},status=200)
		else:
			return JsonResponse({},status=403)
#########################################################################################
		'''
		#print(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		#print(username, password,first_name,last_name,email)
		
		user, se_creo = User.objects.get_or_create(username=username)
		print(user, se_creo)
		
		if se_creo:
			user.set_password(password)
			user.first_name = first_name
			user.last_name = last_name
			user.email = email
			user.save()

			return JsonResponse({},status=200)
		else:
			user = authenticate(username=username, password=password)
			print("El usuario",user,"se autentico")
			return JsonResponse({},status=403)
		
		#user.save()
		#formSpeaker= FormSpeaker(request.POST)
		#userform = UserCreationForm(request.POST)
		#print(userform)
		,defaults={first_name':first_name, 'last_name':last_name,'email':email, 'password':password})
		'''
		