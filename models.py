from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utent(AbstractUser):
    cellphone = models.CharField(max_length=20)