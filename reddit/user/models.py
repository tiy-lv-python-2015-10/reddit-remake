from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)

    def trophy_case(self):
        trophies = self.trophy_set.all()
        return trophies

    @property
    def post_karma(self):
        karma = self.user.votingsystem_set.filter(vote=True, comment=None).count() - \
                     self.user.votingsystem_set.filter(vote=False, comment=None).count()
        return karma

    @property
    def comment_karma(self):
        karma = self.user.votingsystem_set.filter(vote=True, post=None).count() - \
                     self.user.votingsystem_set.filter(vote=False, post=None).count()
        return karma

    @property
    def average_good_karma(self):
        average = self.user.votingsystem_set.filter(vote=True).count() / self.user.votingsystem_set.all().count()
        return average

    @property
    def average_bad_karma(self):
        average = self.user.votingsystem_set.filter(vote=False).count() / self.user.votingsystem_set.all().count()
        return average

    @property
    def total_count(self):
        total = self.user.post_set.all().count() + self.user.comment_set.all().count()
        return total

    def __str__(self):
        return "{}".format(self.user)
