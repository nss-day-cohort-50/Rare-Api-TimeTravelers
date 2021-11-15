from django.db import models

class Subscriptions(models.Model):
    follower_id = models.IntegerField(),
    author_id = models.IntegerField(),
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False),
    ended_on = models.DateTimeField(auto_now=False, auto_now_add=False)