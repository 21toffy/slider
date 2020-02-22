from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class pictures(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.FileField(upload_to='documents/%Y/%m/%d', null= True, blank=True)
