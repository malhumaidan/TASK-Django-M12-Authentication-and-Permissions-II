from django.shortcuts import render, redirect
from django.contrib.auth import login
from users.forms import SignupForm

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

