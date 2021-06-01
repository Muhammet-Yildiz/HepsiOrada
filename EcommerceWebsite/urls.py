

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from customer import views as customerViews
from Main import views
urlpatterns = [

    path('admin/', admin.site.urls),

    path('customer/', include("customer.urls")),

    path('',views.home ,name ="home" ),

    path('ara/',views.search ,name ="search" ),
    path('autocomplete/',views.autocomplete ,name ="autocomplete" ),
    
    path('Categories/', views.category_page ,name ="category"),
    path('Brands/', views.brand_page ,name ="brand"),
    path('contact/', views.contact_page ,name ="contact"),

    path('category-product-list/<slug:cat_slug>', views.category_product_list ,name ="category_product_list"),
    
    path('brand-product-list/<slug:brand_slug>', views.brand_product_list ,name ="brand_product_list"),
    path('product/<slug:slug_text>',views.product_detail, name ="product_detail" ),

    path('addproductlike/<int:product_id>', views.likeproduct ,name ="productlike"),
    
    path('deleteproduct/<int:id>',views.deleteproduct,name="deleteproduct"),
    
    path('filter-data/', views.filterdata ,name ="filterdata"),
    
    path('store/', include("Store.urls")),

    
    path('change_password/', customerViews.change_password ,name ="change_password"),
    path('Account/',customerViews.account ,name="account" ),
    path('Siparişlerim/',customerViews.orders ,name="orders" ),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='ResetPassword/password_reset.html') ,name= 'reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name ='ResetPassword/password_reset_sent.html') ,name='password_reset_done'  ),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='ResetPassword/password_reset_form.html') ,name='password_reset_confirm' ),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name ='ResetPassword/password_reset_done.html') ,name = 'password_reset_complete'),
    path('hasuseremail/', customerViews.hasuseremail ,name ="HasUserEmail"),


    path('addComment/', views.addComment ,name ="addComment"),
    path('evaluate/', views.evaluate ,name ="evaluate"),
    path('commentLikeDislike/', views.commentLikeDislike ,name ="commentLikeDislike"),


    path('teslimat-adreslerim/', customerViews.MyAddresses ,name ="MyAddresses"),
    path('addressDelete/', customerViews.addressDelete ,name ="addressDelete"),
    path('update_profile/', customerViews.updateProfile ,name ="updateProfile"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_title = "En Trend Ürünler Türkiye'nin Online Alışveriş Sitesi HepsiOrada'da  "
admin.site.site_header = " HepsiOrada Admin Paneli"