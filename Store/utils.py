
import json 
from .models import *

from django.shortcuts import get_object_or_404, render 
from django.core.mail import send_mail 
from django.conf import settings 


from django.core.mail import EmailMultiAlternatives 

from django.template.loader import render_to_string 

from django.utils.html import strip_tags 

from django.http import HttpResponse,JsonResponse

def cookieCart(request):

    try : 
        cart = json.loads(request.COOKIES['cart'])
    except : 
        cart = {}

    

    items = []

    order ={'get_cart_total':0 ,'get_cart_items':0 ,'get_cart_oldprice':0}
    
    cartItems =order['get_cart_items']

    for i in cart : 

        try  : 

            cartItems += cart[i]["quantity"]
            
            product = Product.objects.filter(id = cart[i]['productId'] )
            
            for ürün  in product  :
                total = ( ürün.price *  cart[i]['quantity'] )
                
                oldtotal = ( ürün.oldprice *  cart[i]['quantity'] )
             
                order['get_cart_total'] += total 
                order['get_cart_oldprice'] += oldtotal 
                order['get_cart_items'] += cart[i]['quantity']
                
                item = {
                    'product' :{
                        'id':ürün.id ,
                        'title': ürün.title ,
                        'oldprice':ürün.oldprice,
                        'price': ürün.price ,
                        'image' :ürün.image,
                        'brand':ürün.brand,
                        'slug':ürün.slug,
                        'cargotime':ürün.cargotime,
                        'forwardcargotime':ürün.forwardcargotime
                    },
                    'quantity': cart[i]['quantity'] ,
                    'get_total': total,
                    'get_total_oldprice' :oldtotal,
                    'chooseSize':cart[i]["size"],
                    'chooseColor':cart[i]["color"]
                }

                   
                if (ürün.status == False )  :
                    order['shipping'] = True 
                


                items.append(item)
        except :
            pass

    return {
        'items' :items,
        'order':order ,
        'itemsayısı':cartItems
    }



from Store.models import * 

def guestOrder(request, data ) :
    
    addresid = data["chooseAddresId"]
    addresses =get_object_or_404(ShippingAddres ,id =addresid, customer = None )
    newUser =User.objects.create(username = addresses.name+ addresses.surname+ str(addresid) ,password = "123456" ,email = addresses.name +"@gmail.com" ) 
    
    customer = Customer.objects.create( name =addresses.name + addresses.surname ,user = newUser ,email = addresses.name +"@gmail.com" )
    order =Order.objects.create(customer = customer )

    addresses.customer = customer
    addresses.order.add(order)

    addresses.save()


    
    cookieData = cookieCart(request)

    items = cookieData['items']

    for item in items :

        product = Product.objects.get(id =item['product']['id'] )
        
        orderItem = OrderItem.objects.create(
            product = product ,
            order = order ,
            quantity =item['quantity'],
            chooseColor = item['chooseColor'],
            chooseSize = item['chooseSize']
        )

        orderItem.save() 


    return customer ,order 


def  sendCartItems(request) :

    
    customer =Customer.objects.filter(user = request.user)
    for i in customer :
        order = Order.objects.filter(customer=i,complete = False)
        for i in order :
            cartItems =i.get_cart_items

    
    return cartItems



def sendTempEmail(request,SendEmail) :

    to = SendEmail

    content = request.POST.get("content")

    html_content = render_to_string("email_template.html",{'title':'test email 45 baslık ','content':"  "})


    text_content = strip_tags(html_content) 

    email = EmailMultiAlternatives(

        "HepsiOrada' ya Hoşgeldiniz ",
        text_content,
        settings.EMAIL_HOST_USER,
        [to]

    )

    email.attach_alternative(html_content,"text/html")

    email.send()

    return JsonResponse({'sendemail':True})