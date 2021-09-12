from django.contrib import admin
from api.models import product

# Register your models here.
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','image','category','description','price']
