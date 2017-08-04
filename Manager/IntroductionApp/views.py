from django.shortcuts import redirect, render
from django import *
from IntroductionApp import forms, models
from forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User



def index(request):
	context = []
	if request.method == 'POST':
		post_mob = request.POST.get('mobile')
		if post_mob is None:
			post_email = request.POST.get('email')
			post_passw = request.POST.get('password')
			if post_email and post_passw:
				user = authenticate(username=post_email, password=post_passw)
				if user:
					login(request=request, user=user)
					print("hoo")
					return redirect('all_enterprises')
					print("pa")
		else:
			post_email = request.POST.get('email')
			print(post_email)
			post_passw = request.POST.get('password')
			post_mobil = request.POST.get('mobile')
			post_name = request.POST.get('name')

			if (post_email and post_passw and post_mobil and post_name):
				userNou = User.objects.create_user(username=post_email, password=post_passw)
				userProfil = models.UserProfile.objects.create(first_name=post_name, mobile_number = post_mobil, user=userNou)
				return redirect('all_enterprises')

	return render(request, 'index.html', context)
