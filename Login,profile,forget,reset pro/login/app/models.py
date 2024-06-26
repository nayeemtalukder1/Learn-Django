from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  locality = models.CharField(max_length=200)
  mobile = models.IntegerField(default=0)

  def __str__(self):
    return self.name
