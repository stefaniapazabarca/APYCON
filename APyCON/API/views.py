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
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SpeakerRegisterForm
from django.contrib.auth.forms import AuthenticationForm

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

@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
	def post(self, request):
		print(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username= username, password= password)

		#ipdb.set_trace()

		print(user)
		if user:
			return JsonResponse({},status=200)
		else:
			return JsonResponse({},status=400)
