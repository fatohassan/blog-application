from django.shortcuts import render, redirect
from django.urls import reverse
from register.forms import SignUpForm, LogInForm

# Create your views here.
def sign(request):
    sign_form = SignUpForm()
    email_error_empty =''
    if request.POST:
        sign_form = SignUpForm(request.POST)
        if sign_form.is_valid():
            sign_form.save()
            return redirect(reverse('blog_home'))
    context ={'form':sign_form, 'email_error_empty':email_error_empty}
    return render(request, 'register/sign.html', context)

def log(request):
    log_form = LogInForm()
    context = {'form':log_form}
    return render(request, 'register/log.html', context)