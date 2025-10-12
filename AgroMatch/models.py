from django.db import models

class Submission(models.Model):
    soil_type = models.CharField(max_length=20)
    rainfall = models.CharField(max_length=20)
    land_size = models.FloatField()
    phone_number = models.CharField(max_length=15)
    recommendation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.soil_type}"
