from django import forms
from ecogroapp.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=False,max_length=100)
    last_name = forms.CharField(required=False,max_length=100)
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    
