
from django.urls import path
from productapp import views

urlpatterns = [
    path('',views.index),
    path('search',views.search),
    path('addproduct',views.addproduct),
    path('showproduct',views.showproduct),
    path('editproduct/<int:rid>',views.editproduct),
    path('register',views.registration),
    path('adduser',views.adduser),
    path('addrecommendation',views.addrecommendation),
    path('showuser',views.showuser),
    path('edituser/<int:uid>',views.edituser),
    path('login',views.login),
    path('showrecommendation',views.showrecommendation),
]