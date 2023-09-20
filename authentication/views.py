from django.shortcuts import render ,redirect

# Create your views here.
from .forms import RegistrationForm, LoginForm, HomeForm
from django.contrib.auth.models import User

def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            # Do something with the message (e.g., save to database)
            return redirect('home')  # Redirect to the home page
    else:
        form = HomeForm()

    return render(request, 'home.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new User object but don't save it yet
            new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password'],
                                                email=form.cleaned_data['email'])
            # Save the User object
            new_user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Implement authentication logic here
            # For simplicity, let's assume successful login
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
