import datetime

from django.db import models

# Create your models here.
class ExecutedCmd(models.Model):
    cmd=models.CharField(max_length=1024)
    exec_time=models.DateTimeField(default=datetime.datetime.now())
    out=models.CharField(max_length=1024,default='nil')
