from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

class Reply(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    like = models.IntegerField(default=0)