from django.db import models


# Create your models here.

class Cars(models.Model):
    image = models.ImageField(upload_to='cars/')
