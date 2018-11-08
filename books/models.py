from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Books(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    year_pub = models.IntegerField(default=2018)    
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=3,
            validators=[MaxValueValidator(5),
            MinValueValidator(0)])

class PersonalBooks(Books):
    genre = models.CharField(max_length = 20)
    format = models.CharField(max_length = 50, default="Hardcover Book")
