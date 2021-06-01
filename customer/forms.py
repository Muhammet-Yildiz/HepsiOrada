from Store.models import ShippingAddres
from django import forms  
from django.contrib.auth.models import User 

from django.contrib.auth.forms import UserChangeForm ,UserCreationForm

class LoginForm(forms.Form ) :
    email =forms.EmailField(label="email ",widget=forms.EmailInput)
    password = forms.CharField(label="Parola" ,widget=forms.PasswordInput)


class RegisterForm(forms.Form) :

    username =forms.CharField( max_length=200,label="Kullanıcı adı")
    email = forms.EmailField(label="Email",widget=forms.EmailInput )
    password = forms.CharField(max_length=30,label="Parola",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        email =self.cleaned_data.get("email")
        password =self.cleaned_data.get("password")
        usernameError = False

        if (User.objects.filter(username = username ).exists()):
            usernameError = True

        emailError = False
        if (User.objects.filter(email = email ).exists()):
            emailError = True

        
        values = {
            "username" :username ,
            "password": password,
            "email" : email ,
            'emailError' :emailError,
            'usernameError':usernameError
        }

        return values 



from .models import Profile

class UserUpdateForm(UserChangeForm):
    class Meta : 
        model = User 
        fields =['username','email']


class ProfileUpdateForm(forms.ModelForm):
  
    class Meta : 
        model = Profile 
        fields =['birthday','phone','gender']





    

from Store import * 
class ShippingForm(forms.ModelForm):
    class Meta : 
        model =  ShippingAddres
        fields = '__all__'
        exclude = ['customer',"order"]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ad'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Soyad'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+90'}),
            'city': forms.TextInput(attrs={'placeholder': 'Şehir'}),
            'state': forms.TextInput(attrs={'placeholder': 'İlçe'}),
            'neighborhood': forms.TextInput(attrs={'placeholder': 'Mahalle'}),
            'address': forms.Textarea(attrs={'placeholder': 'Mahalle, Sokak, cadde ve diger bilgilerinizi girin'}),
            'title': forms.TextInput(attrs={'placeholder': 'Örnek : Evim ,İş yerim vb.'}),
        }