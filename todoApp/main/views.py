from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from .forms import NewUserForm

# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html')

def register(request):
    # Send form
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:   
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request=request,
                          template_name="main/register.html",
                          context={"form":form})
    # Get page
    form = NewUserForm
    return render(request=request,
          template_name="main/register.html",
          context={"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            # Successful login
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}")
                return redirect("/")
            else:
                # User not in DB
                messages.error(request, "Invalid username or password")
        # Wrongly formatted form
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()

    return render(request=request,
                  template_name= "main/login.html",
                  context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfuly!")
    return redirect("main:homepage")