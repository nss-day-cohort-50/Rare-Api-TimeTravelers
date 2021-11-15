from django.db import models

class Reactions(models.Model):
    label = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    