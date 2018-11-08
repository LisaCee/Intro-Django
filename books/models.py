from django.db import models
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Books(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid4, editable = False)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=3,
            validators=[MaxValueValidator(5),
            MinValueValidator(0)])
