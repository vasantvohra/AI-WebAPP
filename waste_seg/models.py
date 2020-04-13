from django.db import models


# Create your models here.


class Waste_dataset(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='waste/')
    predicted_category = models.CharField(max_length=50, default=None, null=True)
    actual_category = models.CharField(max_length=50, default=None, null=True)
