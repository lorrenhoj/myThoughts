from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def home(request):
    return render(request, 'home.html', {})

# Create your views here.

def login_user(request):
	#Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In")
			return redirect('home') # Import redirect
		else:
			messages.success(request, "There Was An Error Logging In")
			return redirect('login')
	else:
		return render(request, 'login.html', {})