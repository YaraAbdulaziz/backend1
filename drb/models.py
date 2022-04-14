from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Drb(models.Model):
    drb_name = models.CharField(max_length=50)
    drb_host = models.CharField(max_length=15)
    drb_description = models.CharField(max_length=150)
    drb_img = models.ImageField(upload_to='drb/')

    def __str__(self):
        return self.drb_name

class DrbDetail(models.Model):
    DRB_PRICE_CHOICES = (
        ('Price', ' Price'),
        ('Free', 'Free')
    )
    drb_type = models.CharField(max_length=10, choices=DRB_PRICE_CHOICES, default="Free")
    drb_price = models.IntegerField(default=0)
    drb_date = models.DateField()
    drb_duration = models.DateTimeField()
    drb = models.ForeignKey(Drb, on_delete=models.CASCADE, related_name='drb_detail')

    def __str__(self):
        return self.drb.drb_name

class DrbLocation(models.Model):
    drb_location = models.ForeignKey(DrbDetail, on_delete=models.CASCADE, related_name='drb_location')
    drb_location_name = models.CharField(max_length=50)
    drb_lon = models.FloatField()
    drb_lat = models.FloatField()

    def __str__(self):
        return self.drb_location_name