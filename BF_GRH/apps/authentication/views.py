# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,update_session_auth_hash
from .forms import LoginForm, SignUpForm
from django.contrib.auth.forms import PasswordChangeForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


# change password in the app
#def change_password(request):
#    if request.method == 'POST':
#        form =PasswordChangeForm(request.user, request.POST)
#        if form.is_valid():
#            user = form.save()
#            update_session_auth_hash(request, user)
#            messages.info(request, 'Your password was successfully updated')
#            return redirect('home')
#        else:
#            messages.warning(request, 'Something went wrong')
#            return redirect('password-change')
#    else:
#        form = PasswordChangeForm(request.user)
#        context = {'form':form}
#        return render(request, 'accounts/change_password.html', context)
