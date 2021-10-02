from django.db import models

from api.models import category

class Note(models.Model):
    title = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=100,blank=True)
    category = models.ForeignKey(category.Category,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.title
    