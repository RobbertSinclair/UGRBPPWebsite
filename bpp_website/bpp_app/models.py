from django.db import models

# Create your models here.

class MarketingPoints(models.Model):
    header = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=8000, null=False)
    image = models.ImageField(null=True, upload_to="marketing_images", blank=True)

    def __str__(self):
        return self.header

