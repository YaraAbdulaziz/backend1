
from django.contrib import admin

from event.models import *

# Register your models here.

admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(EventLocation)