from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Heading(models.Model):
    heading = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=200, null=True, default=None, blank=True)

    def __str__(self):
        return self.heading

    def save(self, *args, **kwargs):
        self.slug = slugify(self.heading)
        super(Heading, self).save(*args, **kwargs)
        

class MarketingPoints(models.Model):
    heading = models.ForeignKey(Heading, blank=False, default=None, on_delete=models.CASCADE)
    header = models.CharField(max_length=100, null=False)
    text = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, upload_to="marketing_images", blank=True)

    def __str__(self):
        return self.header

class Sponsor(models.Model):
    logo = models.ImageField(null=False, upload_to="sponsor_logos", blank=False)
    link = models.URLField(null=False)





