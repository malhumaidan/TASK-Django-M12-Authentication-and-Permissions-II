from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from users.forms import SigninFrom, SignupForm

# Create your views here.
def user_signup(req):
    form = SignupForm()
    if req.method == "POST":
        form = SignupForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(req, user)
            return redirect("home")
    
    context = {
        "form": form,
    }

    return render(req, "register.html", context)


def user_logout(req):

    
    logout(req)
    return redirect("movie-list")


def user_login(req):
    form = SigninFrom()
    if req.method == "POST":
        form = SigninFrom(req.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(req, auth_user)
                return redirect("home")

    context = {
        "form": form,
    }
    return render(req, "login.html", context)