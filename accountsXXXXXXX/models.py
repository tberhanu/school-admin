from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from adminapp.models import Student
class CustomUser(AbstractUser):
    """" I almost know why all these added attributes, except the Email,
     not displayed in the main admin page. I changed User to CustomUser
     amid the project which is NOT ADVISABLE--mostly creates some bugs.
     So always better to switch at the beginning of the project so that
     we have access to change/add attributes whenever we need. """
    # description = models.CharField(max_length=100, default='')
    # city = models.CharField(max_length=100, default='')
    # website = models.URLField(default='')
    # phone = models.IntegerField(default=0)
    # email = models.EmailField(max_length=254)
    # image = models.ImageField(upload_to='profile_image', blank=True)
    email = models.EmailField(max_length=254)
    # sid = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.email
