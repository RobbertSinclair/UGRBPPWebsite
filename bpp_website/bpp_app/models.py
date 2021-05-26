from django.db import models

# Create your models here.

class Heading(models.Model):
    heading = models.CharField(max_length=100, null=False)

class MarketingPoints(models.Model):
    heading = models.ForeignKey(Heading, blank=False, default=None, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=8000, null=False)
    image = models.ImageField(null=True, upload_to="marketing_images", blank=True)

    def __str__(self):
        return self.header

class Sponsor(models.Model):
    logo = models.ImageField(null=False, upload_to="sponsor_logos", blank=False)
    link = models.URLField(null=False)



