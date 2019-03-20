from django.db import models

class winedata(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    country = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    designation = models.CharField(max_length=100)
    points = models.CharField(max_length=100)
    price = models.IntegerField()
    province = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    region_1 = models.CharField(max_length=100)
    region_2 = models.CharField(max_length=100)
    winery = models.CharField(max_length=100)
    class Meta:
        db_table = "winedataf"

class logininfo(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = "logininfo"