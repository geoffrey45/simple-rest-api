from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Note
from .serializer import NoteSerializer

# a simple GET API View
@api_view(["GET"])
def index(request):
    content = {"message": "Hello World!"}
    return JsonResponse(content)

class Notes(APIView):
    # getting all notes
    def get(self, request, format=None):
        all_notes = Note.objects.all()
        serializers = NoteSerializer(all_notes,many=True)
        return Response(serializers.data)
        #return JsonResponse(serializers.data)

    #adding notes to the database
    def post(self, request, format=None):
        serializers = NoteSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

class singleNote(APIView):
    #get note by id
    def get(self, request,pk, format=None):
        try:
            note = Note.objects.get(pk=pk)
            serializers = NoteSerializer(note)
            return Response(serializers.data)
        except Note.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    #edit note by id
    def put(self, request, pk, format=None):
        note = Note.objects.get(pk=pk)
        serializers = NoteSerializer(note, request.data)
            
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #delete note by id
    def delete(self,request, pk, format=None):
        try:
            note = Note.objects.get(pk=pk)
            note.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
