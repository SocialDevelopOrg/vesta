from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

class Details(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(max_length=20, validators=[phone_regex], blank=False)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.user.first_name+" "+self.pincode

class Events(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    good = models.BooleanField(default=True)
    lon = models.FloatField()
    lat = models.FloatField()
    creator = models.ForeignKey(User)

    def __str__(self):
        return self.creator.first_name+" "+self.title

class Images(models.Model):
    event = models.ForeignKey(Events)
    photo = CloudinaryField('image')