
from django.db import models

class Sigup(models.Model):
    name=models.CharField(max_length=20)
    mobile_no=models.CharField(unique=True,max_length=10)
    email_id =models.EmailField(max_length=15)
    password =models.CharField(max_length=15)