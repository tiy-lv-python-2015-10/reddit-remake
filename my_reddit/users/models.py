# Change len()'s to count()

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile for User on Reddit. Contains karma ratings for posts and comments. Contains int for total number
    of posts."""
    user = models.OneToOneField(User)

    @property
    def post_karma(self):
        """Return int total posts upvotes - downvotes"""
        total = 0
        for post in self.user.post_set.all():
            total += post.karma
        return total

    @property
    def comm_karma(self):
        """Return int total comments upvotes - downvotes"""
        total = 0
        for comment in self.user.comment_set.all():
            total += comment.karma
        return total

    @property
    def avg_up_votes(self):
        """Return float total upvotes / total posts & comments"""
        total = 0
        if (len(self.user.post_set.all()) + len(self.user.comment_set.all())) > 0:
            for post in self.user.post_set.all():
                total += len(post.postupvote_set.all())
            for comment in self.user.comment_set.all():
                total += len(comment.commentupvote_set.all())
            return total / (len(self.user.post_set.all()) + len(self.user.comment_set.all()))
        else:
            return 0

    @property
    def avg_down_votes(self):
        """Return float total downvotes / total posts & comments."""
        if (len(self.user.post_set.all()) + len(self.user.comment_set.all())) > 0:
            total = 0
            for post in self.user.post_set.all():
                total += len(post.postdownvote_set.all())
            for comment in self.user.comment_set.all():
                total += len(comment.commentdownvote_set.all())
            return total / (len(self.user.post_set.all()) + len(self.user.comment_set.all()))
        else:
            return 0

    @property
    def total_use(self):
        """Return int total posts & comments"""
        return self.user.post_set.all().count() + self.user.comment_set.all().count()

    def __str__(self):
        return"{}".format(self.user.username)
