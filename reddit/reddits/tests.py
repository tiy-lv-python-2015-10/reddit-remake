from django.test import TestCase
from .models import Subreddit, Post, Comment
from django.contrib.auth.models import User


class SubredditTestCase(TestCase):

    def setUp(self):
        Subreddit.objects.create(name="Help", description="I'm lost")
        Subreddit.objects.create(name="NOOO", description="I'm lost")
        Subreddit.objects.create(name="asda", description="lkoads")

    def test_current_count(self):
        self.assertEqual(Subreddit.current_count(self), 3)

    def test_today_count(self):
        self.assertEqual(Subreddit.today_count(self), 3)

    def test_daily_average(self):
        self.assertEqual(Subreddit.daily_average(self), .4)


class PostTestCase(TestCase):

    def setUp(self):
        User.objects.create(username='Peter', email="peter@peter.com", password="password", id=1)
        Subreddit.objects.create(name="test subreddit", description="test description")
        Post.objects.create(name="test post", description="test description", subreddit=Subreddit.objects.get(pk=1),
                            user_id=1)
        Post.objects.create(name="test post aswell", description="test description aswell",
                            subreddit=Subreddit.objects.get(pk=1), user_id=1)
        Comment.objects.create(comment_text="this is a test comment", post=Post.objects.get(pk=1), user_id=1)
        Comment.objects.create(comment_text="this is a test comment aswell", post=Post.objects.get(pk=1), user_id=1)
        Comment.objects.create(comment_text="this is a test comment aswell again", post=Post.objects.get(pk=1),
                               user_id=1)

    def test_is_recent(self):
        post1 = Post.objects.get(pk=1)
        post2 = Post.objects.get(pk=2)

        self.assertTrue(post2.is_recent())
        self.assertTrue(post1.is_recent())

    # def test_is_hot(self):
    #     post1 = Post.objects.get(pk=1)
    #     post2 = Post.objects.get(pk=2)
    #
    #     self.assertTrue(post1.is_hot())
    #     self.assertFalse(post2.is_hot())
