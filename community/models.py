from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Details(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone_number = models.CharField(max_length=20, validators=[phone_regex], blank=False)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.user.first_name+" "+self.pincode