from django.db import models

class Subreddit(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    creation_time = models.TimeField()
            #default=timezone.now)
    modification_time = models.TimeField()
            #blank=True, null=True)
    #current_count =
    #today_count =
    #daily_count =

    #GetConnectionsCount

