from django.db import models

class Comments(models.Model):
    
    post_id = models.IntegerField()
    author_id = models.IntegerField()
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)