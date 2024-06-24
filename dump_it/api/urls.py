from django.urls import path
from .views import *

urlpatterns = [
    path('brands/',brand_list_create),
    path('brand/<int:pk>/',brand_description_detail),
    path('categories/',category_list_create),
    path('category/<int:pk>',category_description_detail),
    path('products/',product_list_create),
    path('product/<int:pk>',product_description_detail)
]
