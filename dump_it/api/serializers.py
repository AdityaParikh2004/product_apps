from rest_framework import serializers
from .models import *

class brandserializers(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"