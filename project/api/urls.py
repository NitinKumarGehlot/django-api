from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name="api-overview"),
    path('prod_list/', views.product_list,name="productlist"),
    path('prod_detail/', views.product_details, name="productbyid"),
    path('prod_create/', views.product_create,name="productadd"),
    path('prod_categories/', views.product_categories,name="productallcategory"),
    path('prod_category/', views.product_category,name="productbycategory"),
]
