from django.contrib import admin

# Register your models here.
from .models import PropertyDetails, ScheduledCronjobs

admin.site.register(PropertyDetails)
admin.site.register(ScheduledCronjobs)