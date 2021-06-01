from django.shortcuts import render,redirect,get_object_or_404

from .models import *
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models import Max ,Min
import json 
from datetime import datetime

from Store.models import *
from .filters import ProductFilter

from Store.utils import sendCartItems,cookieCart
from django.contrib.auth.decorators import login_required


from Store.utils import sendCartItems,cookieCart

from django.contrib.auth.decorators import login_required

def evaluate(request) :

    
    productId = request.POST["productid"]
    
    product = get_object_or_404(Product ,id=productId )

    topStar = 0
    all_comment = Comments.objects.filter(product = product)
    for comment in all_comment :
        topStar += comment.star 
    
    if len(all_comment) == 0 :
        averageStar = 0
    else :
        averageStar = float(topStar / len(all_comment))


    customer =Customer.objects.filter(user = request.user)
    for müşteri in customer :
        pass
    
    if (Comments.objects.filter(product =product ,author = request.user).exists()) :
        
        return JsonResponse({  "data":False,'again':True,"productId":productId })


    if(Order.objects.filter(customer=müşteri,complete=True).exists()):
        order = Order.objects.filter(customer=müşteri,complete=True)
        
        for sipariş in order :
            if (OrderItem.objects.filter(order=sipariş,product = product).exists()) :
                orderitem = OrderItem.objects.filter(order=sipariş,product = product)
                for item in orderitem :
                    pass

                return JsonResponse({"data":True, "productId":productId,'averageStar':float(averageStar),'commentNumber' : len(all_comment) , 'productImgurl':product.image.url ,'productName':product.title,  'productSize':item.chooseSize,'productColor':item.chooseColor })

 
    return JsonResponse({  "data":False,"productId":productId })



def addComment(request) :

    if request.method == "POST" :
        author = request.user 
        productid =request.POST['productid']
        içerik =request.POST['içerik']
        star =request.POST['star']

        product = get_object_or_404(Product ,id = productid )
       

        customer =Customer.objects.filter(user = request.user)
        
        for müşteri in customer :
            order = Order.objects.filter(customer=müşteri,complete=True)
        
        for sipariş in order :
            orderitem =OrderItem.objects.filter(order = sipariş ,product =product)

            for a in orderitem :
                comment = Comments.objects.create(product=product , orderitem=a,order = sipariş,author =request.user ,content=içerik,star =star)
    
    return JsonResponse({"data" :True})


def product_detail(request,slug_text ) : 

    product = Product.objects.filter(slug =slug_text )

    for data in product :
        pass

    topStar = 0
    all_comment = Comments.objects.filter(product = data)

    for comment in all_comment :
        topStar += comment.star 
    

    if len(all_comment) == 0 :
        averageStar = 0
    else :
        averageStar = float(topStar / len(all_comment))


    for comment in all_comment :
        
       pass
        
   
    if request.user.is_authenticated : 

        CartItems = sendCartItems(request)

    else :
        cookieData = cookieCart(request)
    
        CartItems = cookieData['itemsayısı']
    
    for data in product :
        
        if request.user.is_authenticated :
        
            if LastReview.objects.filter(product = data).exists() :
                a =LastReview.objects.filter(product = data) 
                for i in a :
                    i.usersee.add(request.user)
                    i.time =datetime.now()
                    i.save()
            else :
                obj = LastReview.objects.create(product =data , review = True )

                obj.usersee.add(request.user)
                obj.save()

        suggest = Product.objects.filter(category=data.category).exclude(id=data.id)[:4]
    
    all_reviews = []
    obj2 = LastReview.objects.all()
    for data in obj2 : 
        if (request.user in data.usersee.all()) :
            all_reviews.append(data)

    context = {
        "product":product,
        "suggest" :suggest,
        "all_reviews": all_reviews,
        'itemsayısı':CartItems,
        'comments':all_comment ,
        'averageStar':averageStar
    }

    return render(request,"product_detail.html",context)




def commentLikeDislike(request) :

    commentId = request.POST['commentId']
    process = request.POST['process']

    comment = get_object_or_404(Comments,id =commentId )

    if (process == "like") : 

        if not(comment.likes.filter(id =request.user.id).exists()) : 

            if comment.dislikes.filter(id =request.user.id).exists():
                comment.likes.add(request.user)
                comment.dislikes.remove(request.user)
            else : 
                comment.likes.add(request.user)
        
        else : 
            comment.likes.remove(request.user) 


    elif (process == "dislike") : 
        if not(comment.dislikes.filter(id =request.user.id).exists()):

            if comment.likes.filter(id =request.user.id).exists():
                comment.likes.remove(request.user)
                comment.dislikes.add(request.user) 
            else :
                comment.dislikes.add(request.user) 
    
        else : 
            comment.dislikes.remove(request.user) 



    data = {
        "likesayı":comment.likes.count(),
        "dislikesayı":comment.dislikes.count()
    }



    return JsonResponse(data)











def autocomplete(request) :

    if 'term' in request.GET : 

        qs = Product.objects.filter(title__istartswith = request.GET.get('term'))[:10]
        results =list() 
        for product in qs : 
            results.append(product.title)
        
        return JsonResponse(results ,safe = False )
    


def search(request) :
    
    if request.user.is_authenticated :

        CartItems = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        CartItems = cookieData['itemsayısı']

    query = request.GET.get("q")

    products = Product.objects.filter(title__contains= query)
    
    cats = Product.objects.distinct().values("category__title","category__id")
    
    brands = Product.objects.distinct().values("brand__title","brand__id")

    colors =  Product.objects.distinct().values("color__title","color__id","color__color_code")

    sizes =  Product.objects.distinct().values("size__title","size__id")

    minMaxPrice = Product.objects.aggregate(Min('price'),Max('price'))

    context = {
        "products" :products ,
        "cats":cats ,
        "colors":colors , 
        "brands":brands,
        "sizes" :sizes,
        "minMaxPrice":minMaxPrice,
        'itemsayısı':CartItems

    }
    return render(request,"search.html",context)

def home(request):


   
    products = Product.objects.all()

    myFilter =ProductFilter(request.GET ,queryset=products)
    products = myFilter.qs

    all_hearts = []

    for product in Product.objects.all() : 

        if(product.heart.filter(id = request.user.id).exists()) :

            all_hearts.append(product)



    brands = Brand.objects.all()

    if request.user.is_authenticated :
       
        customer = request.user.customer

        order ,created =  Order.objects.get_or_create(customer =customer ,complete= False)
 
        items = order.orderitem_set.all()

        itemsayısı = order.get_cart_items

    else :

        items = []
        order ={'get_cart_total':0 ,'get_cart_items':0}

        itemsayısı =order["get_cart_items"]

        try :

            cart = json.loads(request.COOKIES['cart'])
        except :
            cart = {}
        

        for  i in cart  :
            itemsayısı += cart[i]['quantity']



    liste = []
    obj2 = LastReview.objects.all()
    for data in obj2 : 
        if (request.user in data.usersee.all()) :
            liste.append(data)


    context = {
        "products" :products ,
        'itemsayısı':itemsayısı,
        'liste' :liste,
        'allHearts' :all_hearts,
        'brands' :brands,
        'myFilter':myFilter,

    }

    return render(request,"index.html",context)


def brand_product_list(request,brand_slug):
    reviewed = LastReview.objects.all()

    brand = Brand.objects.get(slug =brand_slug)

    data = Product.objects.filter(brand = brand )

    cats = Product.objects.distinct().filter(brand=brand).values("category__title","category__id")
    
    brands = Product.objects.distinct().filter(brand=brand).values("brand__title","brand__id")

    colors =  Product.objects.distinct().filter(brand=brand).values("color__title","color__id","color__color_code")

    sizes =  Product.objects.distinct().filter(brand=brand).values("size__title","size__id")
    
    if request.user.is_authenticated : 

        itemsayısı = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        itemsayısı = cookieData['itemsayısı']


    context = {
        "data" :data ,
        "cats":cats ,
        "colors":colors , 
        "brands":brands,
        "sizes" :sizes,
        "brand_title":brand.title,
        "reviewed":reviewed,
        'itemsayısı' :itemsayısı

    }

    return render(request,"brand-product-list.html",context)








def category_product_list(request, cat_slug) : 

    category = Category.objects.get(slug=cat_slug)

    data = Product.objects.filter(category = category )

    cats = Product.objects.distinct().filter(category=category).values("category__title","category__id")
    
    brands = Product.objects.distinct().filter(category=category).values("brand__title","brand__id")

    colors =  Product.objects.distinct().filter(category=category).values("color__title","color__id","color__color_code")

    sizes =  Product.objects.distinct().filter(category=category).values("size__title","size__id")

    if request.user.is_authenticated : 

        itemsayısı = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        itemsayısı = cookieData['itemsayısı']

    
    context = {
        "data" :data ,
        "cats":cats ,
        "colors":colors , 
        "brands":brands,
        "sizes" :sizes ,
        "cat_title":category.title,
        'itemsayısı':itemsayısı
    }


    return render(request,"category-product-list.html",context)




def category_page(request):

    all_categorys = Category.objects.all()

    if request.user.is_authenticated : 

        itemsayısı = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        itemsayısı = cookieData['itemsayısı']


    context = {
        "Categories" :all_categorys,
        'itemsayısı':itemsayısı
    }

    return render(request ,"category.html",context)




def brand_page(request):
    all_brands = Brand.objects.all()

    if request.user.is_authenticated : 

        itemsayısı = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        itemsayısı = cookieData['itemsayısı']

    context = {
        "Brands" :all_brands,
        'itemsayısı':itemsayısı
    }

    return render(request ,"brand.html",context)








def contact_page(request):

   
    if request.user.is_authenticated : 

        CartItems = sendCartItems(request)
    else :
        cookieData = cookieCart(request)
        CartItems = cookieData['itemsayısı']

    form = ContactForm(request.POST or None )
    if form.is_valid() :
        form2 = form.save(commit=False )

        form2.kullanıcı = request.user

        form2.save()
        messages.success(request,"Mesajınızı aldık .Size en kısa sürede geri dönüş olucaktır .Tesekkurler ")
        return redirect("home")
    else :
        return render(request ,"contact.html",{"form":form ,"itemsayısı":CartItems })





def likeproduct(request,product_id) :

    product = get_object_or_404(Product,id =product_id )

    if product.heart.filter(id =request.user.id).exists() :
        product.heart.remove(request.user)
    else :
        product.heart.add(request.user)

    context ={
        "begenisayısı":product.heart.count(),
    }
    return JsonResponse(context)

@login_required(login_url="login")

def deleteproduct(request,id):

    product =get_object_or_404(Product ,id =id )
    product.heart.remove(request.user.id)
    

    liked =Product.objects.filter(heart =request.user.id)

    
    return JsonResponse({"bool":True,"liked":len(liked)})



def filterdata(request):
  

    colors = request.GET.getlist('color[]')
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    sizes = request.GET.getlist('size[]')

    minprice = request.GET["minPrice"]
    maxprice = request.GET["maxPrice"]

    allProducts = Product.objects.all().order_by("-id").distinct()
    

    allProducts =allProducts.filter(price__gte =minprice)
    allProducts =allProducts.filter(price__lte = maxprice)


    if len(colors)>0 :
        allProducts =allProducts.filter(color__id__in =colors).distinct()
  
    if len(categories)>0 :
        allProducts =allProducts.filter(category__id__in =categories).distinct()
    
  
    if len(brands)>0 :
        allProducts =allProducts.filter(brand__id__in =brands).distinct()
  
    if len(sizes)>0 :
        allProducts =allProducts.filter(size__id__in =sizes).distinct()

    t = render_to_string("ajax-product.html",{'products':allProducts})

    return JsonResponse({"data":t})
