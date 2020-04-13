from django.db import models


# Create your models here.

class Sign_verification_forged(models.Model):
    image = models.ImageField(upload_to='forged_signs/')


class Sign_verification_genuine(models.Model):
    image = models.ImageField(upload_to='genuine_signs/')
