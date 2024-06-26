from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_view
from . forms import LoginForm,MyPasswordReset,MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('', views.home, name='home'),

    path('profile/', views.ProfileView.as_view(),name='profile'),
    path('address/', views.address,name='address'),  
    path('updateaddress/<int:pk>', views.updateAddress.as_view(), name='updateaddress'),

    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login'),

    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', views.LogoutPage, name='logout'),


    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),

    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


]
