from django import forms
from django.db.models import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = '__all__'

class CheckoutForm(forms.ModelForm):
    class Meta: 
        model = Checkout
        fields = '__all__'

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
      