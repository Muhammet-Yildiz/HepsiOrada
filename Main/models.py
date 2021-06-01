from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User 
from django.utils.text import slugify
from EcommerceWebsite.utils import unique_slug_generator 
from django.db.models.signals import pre_save


class Category(models.Model) :

    title = models.CharField(max_length=100)
    image = models.ImageField( upload_to = "category_imgs/",null = True,blank = True )
    slug = models.SlugField(max_length=250,null=True, blank = True )
    def __str__(self):
        return self.title 

    class Meta :
        verbose_name_plural = 'Kategoriler'
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    

def slug_generator(sender,instance, *args ,**kwargs ) : 
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender =Category)




class Brand(models.Model) :

    title = models.CharField(max_length=100)
    image = models.ImageField( upload_to = "brand_imgs/", null=True , blank = True )
    slug =models.SlugField(max_length=200 ,null=True ,blank = True)
    def __str__(self):
        return self.title 
    class Meta :
        verbose_name_plural = 'Markalar'    
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )
    

pre_save.connect(slug_generator,sender =Brand)





class Color(models.Model) :

    title = models.CharField(max_length=100)
    color_code =models.CharField(max_length=100)
    def __str__(self):
        return self.title

    class Meta :
        verbose_name_plural = 'Renk Seçenekleri'
 
    def color_bg(self):
        return mark_safe('<div style="width :50px ;height : 50px ;  border-radius : 10px ;  background: %s " >   </div> ' % (self.color_code) )




class Size(models.Model) :

    title = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

    class Meta :
        verbose_name_plural = 'Boyutlar'





import datetime 
import locale
import random

class Product(models.Model):
    title = models.CharField(max_length=200,verbose_name="Ürün İsmi")
    image= models.ImageField(upload_to = "product_imgs/",verbose_name="Ürün Fotografları " ,null=True ,blank = True)
    slug = models.SlugField(max_length=250,null=True , blank = True)  #url için urun adı gondermek için 
    detail = models.TextField(verbose_name="Ürün Detayı") #ürün detayı 
    specs = models.TextField(verbose_name="Ürün Özellikleri")   #özellikler =specs
    
    category = models.ForeignKey(Category , on_delete =models.CASCADE ,verbose_name="Ürünün Kategorisi")
    
    brand = models.ForeignKey(Brand , on_delete =models.CASCADE ,verbose_name="Ürünün Markası " )
    
    size = models.ManyToManyField(Size ,blank=True ,verbose_name="Mevcut Boyutları")
    color = models.ManyToManyField(Color ,blank=True ,verbose_name="Mevcut Renkleri")
    
    price = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="Fiyat")
    oldprice = models.DecimalField(max_digits=7 ,decimal_places=2 ,verbose_name="Eski Fiyat" )
   
    status = models.BooleanField(default=False,null=True ,blank =False,verbose_name="Ürünün Durumu")
    generalTitle =models.CharField(max_length=200,default=" ")
    heart = models.ManyToManyField(User , blank=True,verbose_name="Begenen Kullanıcılar")

    def __str__(self):
        return self.title
    
    @property   
    def discountRate(self):
        
        total = ((float(self.oldprice) - float(self.price)) / float(self.oldprice)) * 100

        return total
    
    
    @property 
    def cargotime(self) :
        locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')
        now = datetime.datetime.now()
        extra = random.randint(2,5)
        target = now +datetime.timedelta(extra)
        day = target.day
        month =datetime.datetime.strftime(target, '%B')
        return str(day) + " " + month

    def forwardcargotime(self) :
        locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

        now = datetime.datetime.now()

        extra = random.randint(5,10)
        target = now +datetime.timedelta(extra)
        day = target.day
        month =datetime.datetime.strftime(target, '%B')

        return str(day)+ " " + month 



    class Meta :
        verbose_name_plural = 'Ürünler'

   
    
    def image_save(self):
        return mark_safe('<img src ="%s" width="50"  height ="50" /> ' % (self.image.url) )


pre_save.connect(slug_generator,sender =Product)



class ProductImage(models.Model) :
    product = models.ForeignKey(Product,on_delete= models.CASCADE )
    image= models.ImageField(upload_to = "product_imgs/",verbose_name="Ürün Fotosu alternatıf " )

    def __str__(self):
        return self.product.title







class LastReview(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    time = models.DateTimeField(auto_now_add=True,verbose_name="ürün son baktıgım zaman ")
    review = models.BooleanField(default=False)
    # kım gormus bu urunu buna ggore filtreleme yapıcam 
    usersee = models.ManyToManyField(User, blank=True,related_name="usersee")
    def __str__(self):
        return str(self.product)
    class Meta :
        ordering =['-time']
        verbose_name_plural = 'Ürünü son goruntuleme'



class Contact(models.Model): 
    kullanıcı = models.ForeignKey( User , verbose_name= "Kullanıcı adı * ", on_delete=models.CASCADE)
    name = models.CharField(verbose_name = "Ad *" ,max_length=21)
    email = models.EmailField( verbose_name="Email *" )
    message = models.TextField( verbose_name ="Mesajınız *" ) 
    
    def __str__(self):
        return self.name

    class Meta :
        verbose_name_plural = 'İletişim '
from Store.models import Order,OrderItem
class Comments(models.Model) :
    product = models.ForeignKey(Product , on_delete = models.CASCADE ,verbose_name="ürün ")
    author = models.ForeignKey("auth.User",verbose_name="Yorum yazarı ",on_delete = models.CASCADE)
    content = models.TextField(max_length=100 , verbose_name="Yorum ")
    created_date = models.DateTimeField(auto_now_add=True )
    likes = models.ManyToManyField("auth.User",related_name="Related_comment_like" ,blank=True )
    dislikes = models.ManyToManyField("auth.User",related_name="Related_comment_dislike" ,blank=True )
    star = models.DecimalField(max_digits=3,decimal_places=2 ,verbose_name="Star")
    
    order = models.ForeignKey(Order,on_delete=models.CASCADE,blank = True)
    orderitem= models.ForeignKey(OrderItem ,on_delete=models.CASCADE,blank=True ,null=True)
    
    def total_likes(self):
        return self.likes.count()
    def total_dislikes(self):
        return self.dislikes.count()
    
    @property
    def authorhead(self):
        first = str(self.author)[0]
        last =  str(self.author)[-1]
        first = first.upper()
        last = last.upper()
        return first + last

    def __str__(self):
        return self.content  + "    -    "   + str(self.author)


    class Meta : 
        ordering =['-created_date']
