from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#class UserAuthDetails:
#	enrolment_no = models.IntegerField()

class MyProfile(AbstractUser):
    image = models.ImageField(upload_to='myloginsystem/uploads/profile/')
