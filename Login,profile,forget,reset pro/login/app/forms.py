from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from . models import Customer

class CustomerRegistrationForm(UserCreationForm):
  username = forms.CharField()
  email = forms.EmailField()
  password1 = forms.CharField()
  password2 = forms.CharField()

  class Meta:
    model = User
    fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):
  username = UsernameField()
  password = forms.CharField()

class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField()
  new_password1 = forms.CharField()
  new_password2 = forms.CharField()



class MyPasswordReset(PasswordResetForm):
  email = forms.EmailField()
class MySetPasswordForm(SetPasswordForm):
  new_password = forms.CharField()
  confirm_password = forms.CharField()

class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields=['name','locality','mobile']