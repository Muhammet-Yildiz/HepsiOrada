from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404


from django.contrib.auth import login,authenticate,logout


from django.contrib import messages
from  Main.models import Category,Brand,Color,Size,Product,LastReview
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User

from .forms import RegisterForm,LoginForm, ShippingForm

from Store.models import Customer

from Store.utils import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


from Store.models import *


from .forms import UserUpdateForm,ProfileUpdateForm

from .models import Profile
import json

def registerUser(request) :
 
    form = RegisterForm(request.POST or None)

    if  form.is_valid() :

        email =form.cleaned_data.get("email")

        username = form.cleaned_data.get("username")

        password = form.cleaned_data.get("password")

        usernameError = form.cleaned_data.get("usernameError")

        emailError = form.cleaned_data.get("emailError")
        if (emailError and usernameError ):

            messages.info(request,"Bu kullanıcı adı alınmıstır . Lütfen farklı bir adla kayıt olunuz.")

            messages.info(request,"Bu e-posta adresine ait bir hesabınız olduğunu fark ettik. Hesabınıza giriş yapabilir veya hatırlamıyorsanız şifrenizi yenileyebilirsiniz.")

            return redirect('register')
        
        elif (emailError) : 
            messages.info(request,"Bu e-posta adresine ait bir hesabınız olduğunu fark ettik. Hesabınıza giriş yapabilir veya hatırlamıyorsanız şifrenizi yenileyebilirsiniz.")

            return redirect('register')

        elif (usernameError) :

            messages.info(request,"Bu kullanıcı adı alınmıstır . Lütfen farklı bir adla kayıt olunuz.")

            return redirect('register')

      
        else :

            newUser = User(username=username,email=email )
            newUser.set_password(password)
            newUser.save()

            Customer.objects.create(name =username ,email = email , user =newUser)

            Profile.objects.create(user =newUser)

            sendTempEmail(request,email)

            messages.success(request,"Başarıyla kayıt oldunuz  Giriş yapınız ")
      

       
        return redirect("login")

    else :
        context = {
            "form" : form ,
        }
        return render(request,"user/register.html",context)





def logoutUser(request):    

    logout(request) 
    messages.success(request,"Başarıyla cıkış yaptınız ")
    return redirect("home")




def loginuser(request):

    
    form = LoginForm(request.POST or None )
    context = {
        "form" : form 
    }

    if form.is_valid() :

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")


        if (User.objects.filter(email = email).exists()):
            username = User.objects.get(email = email).username
        else :
            username = None

        user =authenticate(username =username,password =password)

        if user is  None :
            messages.info(request,"Email  veya Parola  yanlış ")
            return render(request,"user/login.html",context)
        else :
            messages.success(request,"Başarıyla giriş yaptınız ")
            login(request, user)

            return redirect("home")
 
    else :
    
        return render(request,"user/login.html",context)



@login_required(login_url="login")
def wishlist(request):

    if request.user.is_authenticated : 

        CartItems = sendCartItems(request)
        print("CARTITEMS ------------",CartItems)

    else :
        cookieData = cookieCart(request)
    
        CartItems = cookieData['itemsayısı']


    all_product = []
    alls = Product.objects.all()
    for data in alls : 
        if(data.heart.filter(id =request.user.id).exists()) :
            
            all_product.append(data)
    
    context= {
        "products":all_product,
        "itemsayısı":CartItems
    }

    return render(request,"wishlist.html",context)


@login_required(login_url="login")
def account(request):
 
    CartItems =sendCartItems(request)


    context={
        "itemsayısı":CartItems
    }

    return render(request,"account/account.html",context)




def updateProfile(request):
    CartItems =sendCartItems(request)

    if request.method =="POST" :

        user_form = UserUpdateForm(request.POST,instance =request.user)
        profile_form = ProfileUpdateForm(request.POST,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid() :

            user_form.save() 
            profile_form.save()
            messages.success(request,"Basarıyla bilgiler guncellendi")
            return HttpResponseRedirect('/Account')


    else :
        user_form = UserUpdateForm(instance =request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'user_form':user_form ,
            'profile_form':profile_form,
            "itemsayısı":CartItems

        }
        return render(request,'user/updateProfile.html',context)



    
def change_password(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Parolanız basarıyla guncellendi!')
            return redirect('home')
        else:
            messages.info(request, 'Lütfen asagıdaki hataları duzeltin.')
    else:
        form = PasswordChangeForm(request.user)
    
    context ={
        'form' :form
    }
    return render(request,"account/change_password.html",context)
   
  

def hasuseremail(request) :
    data = json.loads(request.body)
    emailvalue = data['emailvalue']

    total = False 
    if (User.objects.filter(email=emailvalue ).exists()) :
        total = True
    
    else :
        total = False

    return JsonResponse({'data':total} )


def orders(request) :
    
    customer = request.user.customer
    orders  =  Order.objects.filter(customer =customer ,complete= True)

    CartItems = sendCartItems(request)
    

    context = {
        'orders' :orders ,
        'itemsayısı':CartItems
    } 

    return render(request,"account/order.html",context )






def addressDelete(request) :

    shippingId =request.POST['shippingId']
    process = request.POST['process']

    address = get_object_or_404(ShippingAddres, id =shippingId)

    if (process == "delete") :

        address = get_object_or_404(ShippingAddres, id =shippingId)

        address.delete()

    
    return JsonResponse({"data" :True })






def MyAddresses(request) :
    
    if request.method == "POST" :

        form = ShippingForm(request.POST)
        customer =get_object_or_404(Customer ,user =request.user )
        obj = form.save(commit = False)
        obj.customer = customer
        obj.save()
        

        return redirect("MyAddresses")

    else :


        if (request.GET.get("process") ):
            shippingId = request.GET.get("shippingId")
            address = get_object_or_404(ShippingAddres, id =shippingId)
            form = ShippingForm(request.POST or None,instance=address)
            
            
        else :

            form = ShippingForm(request.GET)
            shippingId = None
         


    addresses = ShippingAddres.objects.filter(customer = request.user.customer )

    itemsayısı = sendCartItems(request)
    context = {
        'addresses' :addresses ,
        'form'  :form ,
        'shippingId' :shippingId,
        'itemsayısı':itemsayısı

    }
    
    return render(request,'account/adreslerim.html',context)