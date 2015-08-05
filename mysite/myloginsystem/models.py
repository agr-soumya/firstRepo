from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
# Create your models here.

#class UserAuthDetails:
#	enrolment_no = models.IntegerField()
fs = FileSystemStorage(location = 'media/photos/')
class MyProfile(AbstractUser):
    image = models.ImageField(storage = fs)
