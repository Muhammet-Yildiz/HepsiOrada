


from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.http import JsonResponse
import json 

from .utils import cookieCart ,guestOrder,sendTempEmail

from Main.models import *
from customer.forms import  ShippingForm


from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from django.utils.formats import sanitize_separators



def Cart(request):
    

    if request.user.is_authenticated :
        customer = request.user.customer
        order ,created =  Order.objects.get_or_create(customer =customer ,complete= False)

        items = order.orderitem_set.all()

        cartItems =order.get_cart_items


    else :

        cookieData = cookieCart(request)
    
        cartItems = cookieData['itemsayısı']

        items = cookieData['items']

        order = cookieData['order']

    obj = LastReview.objects.all()
    liste = []
    for data in obj :
        if ( request.user in data.usersee.all()) :
            liste.append(data)


    user_hearts = []
    alls = Product.objects.all()
    for data in alls : 
        if(data.heart.filter(id =request.user.id).exists()) :
            user_hearts.append(data)
    
    context = {
        'items' :items,
        'order':order ,
        'itemsayısı':cartItems,
        'liste':liste,
        "user_hearts":user_hearts,

        
    }
    return render(request,"store/sepetim.html",context)


def Checkout(request) :

   
    if request.user.is_authenticated :

        customer = request.user.customer
        order ,created =  Order.objects.get_or_create(customer =customer ,complete= False)

        items = order.orderitem_set.all()
        cartItems =order.get_cart_items


        addresses =ShippingAddres.objects.filter(customer = customer)

        if request.method == "POST" :
            form = ShippingForm(request.POST)
            customer =get_object_or_404(Customer ,user =request.user )
            obj = form.save(commit = False)
            obj.customer = customer
            obj.save()
            return redirect("checkout")

        else :
            form = ShippingForm()

        context = {
            'items' :items,
            'order':order ,
            'itemsayısı':cartItems,
            'addresses':addresses,
            'form':form
        }

    else :
        cookieData = cookieCart(request)
    
        cartItems = cookieData['itemsayısı']

        items = cookieData['items']

        order = cookieData['order']


        if request.method == "POST" :
            form = ShippingForm(request.POST)
            if form.is_valid():
                form.save()
            
            return HttpResponseRedirect('/store/checkout')

        else :
            form = ShippingForm(request.GET)
            try :
                addresses =ShippingAddres.objects.filter(customer = None)
            except :
                addresses = {}


        context = {
            'items' :items,
            'order':order ,
            'itemsayısı':cartItems,
            'form':form,
            'addresses':addresses
            
        }

  
    return render(request,"store/ödeme.html",context)





def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    chooseSize = data['chooseSize']
    chooseColor = data['chooseColor']

    
    customer = request.user.customer 

    product = get_object_or_404(Product, id= productId )
    order  = get_object_or_404(Order, customer =customer ,complete = False)
    
    if (OrderItem.objects.filter(order = order, product =product,orderStatus=False).exists()) :

            if (OrderItem.objects.filter(order = order ,product =product,chooseSize =chooseSize ,chooseColor=chooseColor,orderStatus=False).exists()) :

                orderItem = get_object_or_404(OrderItem,product =product, order=order , chooseSize = chooseSize ,chooseColor=chooseColor )
               
                if action == 'add':

                    orderItem.quantity = (orderItem.quantity + 1 )

                elif action == 'remove':
                    orderItem.quantity = (orderItem.quantity - 1 )

                elif action == 'allremove' :
                    orderItem.quantity = 0

                orderItem.save()


                if orderItem.quantity <=0 :
                    orderItem.delete()


            else  : 

                orderItem  = OrderItem.objects.create(order=order , product = product )

                orderItem.chooseSize = chooseSize
                orderItem.chooseColor = chooseColor

                if action == 'add':
                    orderItem.quantity = (orderItem.quantity + 1 )

                elif action == 'remove':
                    orderItem.quantity = (orderItem.quantity - 1 )

                orderItem.save()
    else :

            orderItem   = OrderItem.objects.create(order=order , product = product )

            orderItem.chooseSize = chooseSize
            orderItem.chooseColor = chooseColor

            if action == 'add':
                orderItem.quantity = (orderItem.quantity + 1 )

            elif action == 'remove':
                orderItem.quantity = (orderItem.quantity - 1 )

         
            orderItem.save()


            if orderItem.quantity <=0 :
                orderItem.delete()
    

    return  JsonResponse({'bool':True},safe =False )




def processOrder(request) :

    transaction_id = datetime.now().timestamp()

    data = json.loads(request.body)

    if request.user.is_authenticated : 

        customer = request.user.customer 
      
        order ,created  = Order.objects.get_or_create(customer = customer ,complete = False )
    
    
        if order.shipping == True  : 

            addresid = data["chooseAddresId"]

            shippingAddres =get_object_or_404(ShippingAddres,id = addresid)
            
            shippingAddres.order.add(order)

            
            shippingAddres.save()

          

    else :
        customer ,order = guestOrder(request ,data)



    total = data["total"]


    order.transaction_id = transaction_id
    
    if  float( sanitize_separators(total)) == float( order.get_cart_total ) :
        order.complete = True

    all_orderitem = order.orderitem_set.all()


    for orderItem in all_orderitem :
        orderItem.orderStatus = True
        orderItem.save()

    order.save()
    
  
    return  JsonResponse('sipariş alındı ',safe =False )


