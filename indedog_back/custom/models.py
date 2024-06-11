# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
class Avatar(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, blank=True)
    job = models.CharField(max_length=20, blank=True)