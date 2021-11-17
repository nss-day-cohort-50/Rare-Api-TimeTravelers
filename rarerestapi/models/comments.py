from django.db import models

class Comments(models.Model):
    
    post_id = models.ForeignKey("Posts", on_delete=models.CASCADE)
    author_id = models.ForeignKey("RareUsers", on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)