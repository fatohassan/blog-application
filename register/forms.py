from django import forms
from django.utils.translation import gettext_lazy as _
from register.models import SignUp, LogIn

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
        fields = '__all__'
        labels = {
            'user_name':_('User Name'),
            'email':_('Email'),
            'password':_('Password'),
            'confirm_password':_('Confirm Password')
        }
        # error_messages = {

        # }
class LogInForm(forms.ModelForm):
    class Meta:
        model = LogIn
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = '__all__'
        labels = {'user_name':_('User Name'),
                  'password':_('Password'),

        }