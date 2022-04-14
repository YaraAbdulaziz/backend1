from django.db import models
from distutils.command.upload import upload

# Create your models here.

class Event(models.Model):
    ev_name = models.CharField(max_length=50)
    ev_host = models.CharField(max_length=15)
    ev_description = models.CharField(max_length=150)
    ev_img = models.ImageField(upload_to='event/')

    def __str__(self):
        return self.ev_name

class EventDetail(models.Model):
    EV_PRICE_CHOICES = (
        ('Price', ' Price'),
        ('Free', 'Free')
    )
    ev_type = models.CharField(max_length=10, choices=EV_PRICE_CHOICES, default="Free")
    ev_price = models.IntegerField(default=0)
    ev_date = models.DateField()
    ev_duration = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ev_detail')

    def __str__(self):
        return self.event.ev_name

class EventLocation(models.Model):
    event_location = models.ForeignKey(EventDetail, on_delete=models.CASCADE, related_name='event_location')
    ev_location_name = models.CharField(max_length=50)
    ev_lon = models.FloatField()
    ev_lat = models.FloatField()

    def __str__(self):
        return self.ev_location_name