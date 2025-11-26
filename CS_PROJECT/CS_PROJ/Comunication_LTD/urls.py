from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('loginYAY/', views.loginYAY, name= 'loginYAY'),
    path('loginFailed/',views.login_req, name= 'login_req'),

    path('register/', views.register, name= 'register'),
    path('register/Confirm/', views.registerConfirm, name= 'registerConfirm'),
    path('register/Failed/', views.register_req, name= 'register_req')
]