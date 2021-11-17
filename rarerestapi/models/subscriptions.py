from django.db import models

class Subscriptions(models.Model):
    follower_id = models.ForeignKey("RareUsers", on_delete=models.CASCADE, related_name="follower")
    author_id = models.ForeignKey("RareUsers", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    ended_on = models.DateTimeField(auto_now=False, auto_now_add=False)