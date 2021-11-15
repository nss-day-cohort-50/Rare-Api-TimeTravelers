from django.db import models

class Posts(models.Model):
    
    user_id = models.IntegerField("RareUsers"),
    category_id = models.IntegerField("Categories"),
    title = models.CharField(max_length=50),
    publication_date = models.DateField(auto_now=False, auto_now_add=False),
    image_url = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None),
    content = models.CharField(max_length=500),
    approved = models.BooleanField(default=False)