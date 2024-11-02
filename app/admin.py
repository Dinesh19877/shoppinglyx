from django.contrib import admin

from .models import(
    customer,product,card,orderPlace
)

@admin.register(customer)
class customermodeladmin(admin.ModelAdmin):
    list_display = ["id","user","name","localtiy","city","zipcode","state"]
    
@admin.register(product)
class productmodeladmin(admin.ModelAdmin):
    list_display = ["id","title","selling_price","dicount","description","brand","category","pruduct_image"]
    
@admin.register(card)
class cardmodeladmin(admin.ModelAdmin):
    list_display = ["id","user","product","quantiy"]
    
@admin.register(orderPlace)
class orderPlacemodeladmin(admin.ModelAdmin):
    list_display = ["id","user","customer","product","quantiy","ordered_date","status"]