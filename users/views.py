# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class SignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


# def logout(request):
#     return
def change_password(request):
    if request.method == 'POST':
        """ Here 'data' and 'user' are important to be mentioned. """
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            """ To make sure user still logged in after changing the password and being
            to redirected to the new page."""

            update_session_auth_hash(request, form.user)
            return render(request, 'users/post_password_change.html')
        else:
            return redirect(reverse('users:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'users/change_password.html', args)

def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        args = {'form': form}

        if form.is_valid():
            form.save()
            flag = True
            return render(request, 'users/post_signup.html', {'signedup': True})
        else:

            return render(request, 'users/signup.html', args)

    else:
        form = CustomUserCreationForm()
        args = {'form': form}
        return render(request, 'users/signup.html', args)
