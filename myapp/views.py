from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def signup_account(request):
    if request.method == "POST":
        # Get form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate inputs
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')

        # Create and save user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        # Display success message and redirect
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('login')

    # Render the signup form
    return render(request, 'signup.html')


def login_account(request):
    if request.method == "POST":
        # Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('todo')
        else:
            # Invalid credentials
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    # Render the login form
    return render(request, 'login.html')


@login_required(login_url='login')  # Redirects to the login page if the user is not logged in
def todo(request):
    return render(request, 'todo.html')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    return redirect('login')  # Replace 'login' with the URL name of your login page
