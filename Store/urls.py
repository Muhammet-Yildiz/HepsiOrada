
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    path('sepetim/',views.Cart ,name="cart" ),
    path('checkout/',views.Checkout ,name="checkout" ),
    path('update_item/',views.updateItem ,name="updateItem" ),
    path('process_order/',views.processOrder ,name="processOrder" ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

