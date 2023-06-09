from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm




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
	

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return render(request, 'home.html', {})



def register_user(request):
	return render(request, 'register.html', {})


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})
	return render(request, 'register.html', {'form':form})


def blog(request):
	return render(request, 'blog.html', {})