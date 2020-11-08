from django.db import models

# Create your models here.
class Book(models.Model):
    BookName = models.CharField(max_length=35)
    Edition = models.IntegerField()
    AuthorName = models.CharField(max_length=25)
    Publication = models.CharField(max_length=25)
    BookCategory = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
    user_id = models.IntegerField()