from rest_framework import serializers
from .models import Note

#note model serializer
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','title','body','date')