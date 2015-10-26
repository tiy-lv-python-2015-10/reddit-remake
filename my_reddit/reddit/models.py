from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from users.models import Profile


class Subreddit(models.Model):
    """
    Category for Posts
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        """Return int number of posts"""
        return self.post_set.all().count()

    def today_count(self):
        """Return int number of posts for today"""
        day = timezone.now() - timezone.timedelta(days=1)
        return self.post_set.all().filter(posted_at__gte=day).count()

    def daily_average(self):
        """Return float daily average number of posts"""
        week = timezone.now() - timezone.timedelta(days=7)
        return (self.post_set.all().filter(posted_at__gte=week).count()) / 7

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    """
    Posts, keys to Subreddit and User
    """
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    url = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=50)
    subreddit = models.ForeignKey(Subreddit)
    user = models.ForeignKey(User)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def karma(self):
        """Return int single post upvotes - downvotes"""
        return self.postupvote_set.all().count() - self.postdownvote_set.all().count()

    def is_recent(self):
        """Return boolean if posted within 24 hours"""
        return timezone.now() - timezone.timedelta(days=1) <= self.posted_at

    def is_hot(self):
        """Return boolean true if commented on more than 3 times within 3 hours"""
        three_hours = timezone.now() - timezone.timedelta(hours=3)
        count = self.comment_set.all().filter(posted_at__gte=three_hours).count()
        if count > 3:
            return True
        else:
            return False

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    """Comment class keys to User and Post"""
    comment_text = models.TextField(max_length=1000)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    posted_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def karma(self):
        """Return int single comment upvote - downvote"""
        return self.commentupvote_set.all().count() - self.commentdownvote_set.all().count()

    def __str__(self):
        return "{}".format(self.comment_text[:32])


class PostUpVote(models.Model):
    """This class and 3 classes below: Timestamps for upvotes and downvotes"""
    post_up_vote = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class PostDownVote(models.Model):
    post_down_vote = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class CommentUpVote(models.Model):
    comm_up_vote = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment)


class CommentDownVote(models.Model):
    comm_down_vote = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment)


class Trophy(models.Model):
    """Trophies for Users"""
    profile = models.ManyToManyField(Profile)
    name = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
