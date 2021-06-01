from django.contrib import admin
from django.urls import path,include

from . import views 


urlpatterns = [
    path('wishlist/', views.wishlist ,name ="wishlist"),
    path('login/', views.loginuser,name ="login"),
    path('logout/', views.logoutUser ,name ="logout"),
    path('register/', views.registerUser ,name ="register"),

]
