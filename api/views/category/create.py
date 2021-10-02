from rest_framework import serializers
from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.response import  Response
from api.models.category import Category
from api.serializers.category import CategorySerializer
from rest_framework import serializers, status, permissions

@api_view(["POST","GET"])
def category(request,version):
    if request.method == "GET":
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response({"data" : serializer.data})
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "errors": None, "status_code": 0,
                             "status_message": "successfully saved category details",
                             "message": "You have successfully saved category"}, status=status.HTTP_201_CREATED)