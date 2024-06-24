from rest_framework import serializers
from .models import *

class brandserializers(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"
        
class categoriesserializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"
        
class productserializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"