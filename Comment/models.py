from django.db import models

class Comment(models.Model):
    id = models.UUIDField()
    comment_text = models.TextField(max_length=255)
    #relationship_to_user =
    #relationship_to_post =
    creation_time = models.TimeField()
            #default=timezone.now)
    modification_time = models.TimeField()
            #blank=True, null=True)
