from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  age = models.IntegerField(default=0,blank=True)
  img = models.ImageField(upload_to='profile-image/', blank=True)
  bio = models.TextField()


  def __str__(self):
      return self.user.username