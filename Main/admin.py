from django.contrib import admin

from .models import * 


admin.site.register(ProductImage)



admin.site.register(Size)

admin.site.register(Contact)

admin.site.register(Comments)




@admin.register(LastReview)
class LastReviewAdmin(admin.ModelAdmin):
    list_display= ["id","product","time","review"]
    list_display_links = ["product","id"]
    list_editable = ["review"]

    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display= ["id","title","image_save"]
    list_display_links = ["id","title","image_save"]

    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= ["id","title","image_save"]
    list_display_links = ["id","title","image_save"]

    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ["image_save","title","price","status","brand","category","slug"]
    list_display_links = ["image_save" ,"title"]
    list_filter = ["brand"]
    list_editable = ["status"]
    filter_horizontal = ["color","heart","size"]
    def get_products(self, obj):
        return "\n".join([p.color for p in obj.color.all()])



@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display= ["id","title","color_bg" ,"color_code"]
    list_display_links = ["id","title"]



