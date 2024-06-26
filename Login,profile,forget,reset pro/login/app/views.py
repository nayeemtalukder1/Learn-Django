from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import logout

from . models import Customer
from . forms import CustomerRegistrationForm,CustomerProfileForm

# Create your views here.


def home(request):
  return render(request,'index.html')


class CustomerRegistrationView(View):
  def get(self,request):
    form = CustomerRegistrationForm()
    return render(request,'customerregistration.html',locals())
  def post(self,request):
    form = CustomerRegistrationForm(request.POST)
    form.save()


class ProfileView(View):
  def get(self,request):
    form = CustomerProfileForm()
    return render(request,'profile.html',locals())
  def post(self,request):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      user = request.user
      name = form.cleaned_data['name']
      locality = form.cleaned_data['locality']
      mobile = form.cleaned_data['mobile']

      reg = Customer(user=user,name=name,locality=locality,mobile=mobile)
      reg.save()
    return render(request,'profile.html',locals())
  
def address(request):
  add = Customer.objects.filter(user=request.user)
  return render(request,'address.html',locals())

class updateAddress(View):
  def get(self,request,pk):
    add = Customer.objects.get(pk=pk)
    form = CustomerProfileForm(instance=add)
    return render(request,'updateaddress.html',locals())
  def post(self,request,pk):
    form = CustomerProfileForm(request.POST)
    if form.is_valid():
      add = Customer.objects.get(pk=pk)
      add.name = form.cleaned_data['name']
      add.locality = form.cleaned_data['locality']
      add.mobile = form.cleaned_data['mobile']
      add.save()
    return redirect('address')
  
def LogoutPage(request):
  logout(request)
  return redirect('login')
  

