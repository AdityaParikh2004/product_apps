from rest_framework import status
from rest_framework.views import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def brand_list_create(request):
    if request.method == "GET":
        route_descriptions = Brands.objects.all()
        serializers = brandserializers(route_descriptions, many=True)
        return Response(
            {"success": True,
             "message": "Created successfully",
             "data": serializers.data,
             },
            status=status.HTTP_200_OK
        )
    elif request.method == "POST":
        serializers = brandserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(
                {
                    "success": True,
                    "message": "Created successfully",
                    "data": serializers.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": True,
                "message": "Validation error",
                "errors": serializers._errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        
@api_view(["GET", "PUT", "DELETE"])
def brand_description_detail(request, pk):
    route_description = get_object_or_404(Brands, pk=pk)

    if request.method == "GET":
        serializer = brandserializers(route_description)
        return Response(
            {
                "success": True,
                "message": "Retrieve Successful",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    elif request.method == "PUT":
        serializer = brandserializers(
            route_description, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Updated Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"success": False, "message": "Invalid data provided."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    elif request.method == "DELETE":
        route_description.delete()
        return Response(
            {"success": True, "message": "Deleted successfully."},
            status=status.HTTP_200_OK,
        )
