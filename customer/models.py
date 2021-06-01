from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER = (
    ('male', 'erkek'),
    ('female', 'kadın'),
    )
    user = models.OneToOneField(User,on_delete= models.CASCADE, verbose_name ="Kullanıcı"  )
    gender = models.CharField(max_length=50, choices=GENDER, verbose_name="Cinsiyet", blank=True )
    birthday=models.CharField( null=True, blank=True,max_length=15,verbose_name="Dogum Tarihi")
    phone = models.CharField(max_length=50 ,verbose_name="Cep Telefonu", blank=True)
    def __str__(self):
        return  self.user.username 
    
    class Meta :
        verbose_name_plural = 'Profile'


