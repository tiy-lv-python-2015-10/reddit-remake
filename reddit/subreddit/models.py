import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Subreddit(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length= 255, default='empty')
    creation_date_time = models.DateField(auto_now_add=True)


    # def current_count(self):
    #     #that returns how many posts
    # def today_count(self):
    #     #that returns posts in the last 24 hours
    # def daily_average(self):
    #     #gets the average count of posts over the last 7 days

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255, default='empty')
    #url: which can be null and should use the built in urlfield type
    #slug: This is a url friendly version of the title. SlugField
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subreddit_rel = models.ForeignKey(Subreddit)

    # def is_recent(self):
    #      return timezone.now() - datetime.timedelta(days=1) <= self.creation_time
    #
    # def is_hot(self):
    #     #returns True/False if the post has gotten more than 3 comments in the past 3 hours
    #     if timezone.now() - datetime.timedelta(hours=3) <= self.creation_time:
    #         return True
    #     else:
    #         return False

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.CharField(max_length= 255, default='empty')
    user_rel = models.ForeignKey(User)
    post_rel = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)



