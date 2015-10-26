from django.test import TestCase
from .models import Subreddit, Post, Comment, PostUpvote, CommentUpvote, Trophies
from django.contrib.auth.models import User

# Create your tests here.
class SubredditTestCase(TestCase):

    def setUp(self):

    def test_current_count(self):


    def test_today_count(self):


    def test_daily_average(self):

class PostTestCase(TestCase):

     def setUp(self):


class CommentTestCase(TestCase):

     def setUp(self):

class PostUpvoteTestCase(TestCase):

     def setUp(self):

class CommenttUpvoteTestCase(TestCase):

     def setUp(self):

class TrophiesTestCase(TestCase):

     def setUp(self):