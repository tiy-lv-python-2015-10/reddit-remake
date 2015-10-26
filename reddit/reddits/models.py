from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from user.models import Profile


class Subreddit(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        return self.post_set.all().count()

    def today_count(self):
        one_day = timezone.now() - datetime.timedelta(days=1)
        return self.post_set.filter(creation_time__gte=one_day).count()

    @property
    def daily_average(self):
        one_week = timezone.now() - datetime.timedelta(days=7)
        weekly_post = self.post_set.filter(creation_time__gte=one_week).count()
        weekly_post /= 7
        weekly_post = round(weekly_post, 1)
        return weekly_post

    def __str__(self):
        return "{} posted on {}".format(self.name, self.created)


class Post(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)

    def is_recent(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.creation_time

    @property
    def is_hot(self):
        three_hours = timezone.now() - datetime.timedelta(hours=3)
        comments = self.comment_set.filter(created_time__gte=three_hours).count()
        if comments >= 3:
            return True
        else:
            return False

    def karma(self):
        karma = self.votingsystem_set.filter(vote=True).count() - self.votingsystem_set.filter(vote=False).count()
        return karma

    def __str__(self):
        return "{} {}".format(self.name, self.creation_time)


class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def karma(self):
        karma = self.votingsystem_set.filter(vote=True).count() - self.votingsystem_set.filter(vote=False).count()
        return karma

    def __str__(self):
        return "{} posted by {} on {}" .format(self.id, self.user, self.created_time)


class VotingSystem(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, null=True, blank=True)
    comment = models.ForeignKey(Comment, null=True, blank=True)
    vote = models.NullBooleanField()
    time_made = models.DateTimeField(auto_now_add=True)

class Trophy(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(Profile)
    obtained = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} earned by {} on {}".format(self.name, self.user, self.obtained)
