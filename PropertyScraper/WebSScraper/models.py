from django.db import models

# Create your models here.
class PropertyDetails(models.Model):
    # id - first parameter
    # property_name, property_cost, property_type, property_locality, property_city, property_area
    property_name = models.CharField(max_length=200)
    property_cost = models.CharField(max_length=200)
    property_type = models.CharField(max_length=200)
    property_locality = models.CharField(max_length=1000)
    property_city = models.CharField(max_length=100)
    property_area = models.CharField(max_length=1000)

    def __str__(self):
        return str("".join([self.property_name, self.property_cost, self.property_type, self.property_locality, self.property_city, self.property_area]))
    
    # Username: admin
    # Email address: admin@example.com
    # Password: password@example

class ScheduledCronjobs(models.Model):
    time = models.TimeField()

    def __str__(self):
        return str(self.time)