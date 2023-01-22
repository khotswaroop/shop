from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from productapp.models import Product,UserModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields='__all__'

# class RecommendationForm(forms.ModelForm):
#     class Meta:
#         model=Product
#         fields='__all__'
