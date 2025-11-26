from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login_req, name= 'login_req'),
    
    path('loginYAY/', views.loginYAY, name= 'loginYAY'),
    path('loginFailed/',views.login_req, name= 'loginFailed'),

    path('register/', views.register, name= 'register'),
    path('registerConfirm/', views.register_req, name= 'register_req'),

    path('registerFailed/', views.registerFailed, name= 'registerFailed')
]