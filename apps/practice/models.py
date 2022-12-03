# import os, django
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestToolsSetting.settings.settings")
# django.setup()
from django.db import models


# Create your models here.
class APIInfo(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=2000)
    apiType = models.CharField(max_length=10)
    apiParamsType = models.CharField(max_length=10)
    apiParams = models.CharField(max_length=500)
    header = models.CharField(max_length=1500, default="")
    responseDaa = models.CharField(max_length=2500, default="")
    isDel = models.IntegerField(default=0)
    ctime = models.DateTimeField(auto_now=True)
    utime = models.DateTimeField(auto_now=True)
    remark = models.CharField(max_length=2500, default="")

    class Meta:
        db_table = 'apiRecord'
