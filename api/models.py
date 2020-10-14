from django.db import models

#note model
class Note(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.title