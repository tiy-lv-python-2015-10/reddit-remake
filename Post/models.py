from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.UUIDField()
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    url = models.URLField(max_length=200)
    slug = models.SlugField(max_length=50)
    creation_time = models.TimeField()
            #default=timezone.now)
    modification_time = models.TimeField()
            #blank=True, null=True)
    #relationship_to_subreddit =
    #relationship_to_a_user =
    #is_recent
    #is_hot