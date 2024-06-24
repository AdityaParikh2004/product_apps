from django.urls import path
from .views import *

urlpatterns = [
    # path('',DumpItAPI.as_view()),
    # path('create/',DumpItAPI.as_view()),
    path('brands/',brand_list_create),
    path('brand/<int:pk>/',brand_description_detail)
]
