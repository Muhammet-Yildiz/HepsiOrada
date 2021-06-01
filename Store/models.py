
from django.db import models

from django.contrib.auth.models import User 


class Customer(models.Model) : 
    user =models.OneToOneField(User ,on_delete =models.CASCADE , null= True ,blank = True )
    name =models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name


class Order(models.Model) : 
    customer = models.ForeignKey(Customer ,on_delete =models.SET_NULL ,null=True ,blank = True ,verbose_name="Müsteri Ad" )
    dateOrdered = models.DateTimeField(auto_now_add=True )
    complete = models.BooleanField(default=False ,null= True ,blank=False ,verbose_name="Sipariş Durumu")
    transaction_id = models.FloatField(max_length=200 , null= True )
    
    def __str__(self):
        return str(self.id) + ' :  '+str(self.customer )
    class Meta :
        ordering =['-transaction_id']

    @property   
    def shipping(self):
        shipping = False 
        orderitems =self.orderitem_set.all()

        for item in orderitems :
            if (item.product.status == False ) :
                shipping = True 

        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total =sum([item.get_total for item in orderitems])
        return total 
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total =sum([item.quantity for item in orderitems])

        return total
        
    @property
    def get_cart_oldprice(self):
        orderitems = self.orderitem_set.all()
        toplam =0 
        for i in orderitems :
            toplam += (i.product.oldprice * i.quantity)

        return toplam 

    @property
    def customerHead(self) :
        first = str(self.customer)[0]
        last =  str(self.customer)[-1]
        first = first.upper()
        last = last.upper()
        return first + last

      


from Main.models import Product
class OrderItem(models.Model) : 
    product = models.ForeignKey(Product ,on_delete =models.CASCADE ,null=True ,blank = True )
    order = models.ForeignKey(Order ,on_delete =models.SET_NULL ,null=True ,blank = True )
    quantity = models.IntegerField(default=0 ,null=True , blank= True )   
    date_added = models.DateTimeField(auto_now_add=True )

    chooseSize =models.CharField( max_length=25,null=True,verbose_name="Seçilen Boyut")
    chooseColor =models.CharField( max_length=20,null=True,verbose_name="Seçilen Renk")
    orderStatus = models.BooleanField(default=False,null=True ,blank =False,verbose_name="ürün satıldıysa evet satılmadıysa hayır durumundadır ")

    def __str__(self):
        return str(self.product)+" - "+str(self.order.customer)

    @property
    def get_total(self) :
        total = self.product.price * self.quantity
        return total 
    
    @property
    def get_total_oldprice(self) :
        total = self.product.oldprice * self.quantity
        return total 


class ShippingAddres(models.Model) : 
  
    name = models.CharField(max_length=200,null=True ,verbose_name="")
    surname = models.CharField(max_length=200 ,verbose_name="",null=True )
    phone_number =models.CharField(max_length=12 , null=True ,blank=True ,verbose_name="Telefon ")
    customer = models.ForeignKey(Customer ,on_delete =models.SET_NULL ,null=True ,blank = True )
    city = models.CharField(max_length=200 ,null=False,verbose_name="Şehir")
    state = models.CharField(max_length=200 ,null=False ,verbose_name="İlçe")
    neighborhood =models.CharField(max_length=200 ,null=False, verbose_name="Mahalle")
    address =models.TextField(max_length=200,null= False ,verbose_name="Adres Bilgisi ")
    title = models.CharField(max_length =100 ,null = True ,verbose_name = "Adres Başlıgı "  )
    order = models.ManyToManyField(Order ,blank=True )
    
   
    date_added = models.DateTimeField(auto_now_add=True )
    def __str__(self):
        return self.address +"  --    " +  str(self.customer) + ' === ' + str(self.id)








