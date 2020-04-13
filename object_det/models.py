from django.db import models

# Create your models here.

class Video(models.Model):
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
