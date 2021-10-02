from django.db.models import fields
from rest_framework import serializers
from api.models.category import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id","title")

    def save(self,*args, **kwargs):
        category = Category(
            title = self.validated_data["title"]
        )
        category.save()
        return category