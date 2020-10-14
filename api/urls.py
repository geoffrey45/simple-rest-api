from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('notes', views.Notes.as_view()),
    path('notes/<pk>', views.singleNote.as_view())
]