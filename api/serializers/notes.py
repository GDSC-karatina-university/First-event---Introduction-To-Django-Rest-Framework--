from django.db.models import fields
from rest_framework import serializers
from api.models.notes import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("title","description","category")

    def save(self,*args, **kwargs):
        note = Note(
            title = self.validated_data["title"],
            description = self.validated_data["description"],
            category = self.validated_data["category"]
        )
        note.save()
        return note