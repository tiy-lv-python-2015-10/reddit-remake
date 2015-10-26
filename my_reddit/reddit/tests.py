from django.contrib.auth.models import User
from django.test import TestCase

from reddit.models import Subreddit, Post, Comment, PostUpVote, PostDownVote, CommentUpVote, CommentDownVote


class TestSubreddit(TestCase):

    def setUp(self):
        pete = User.objects.create_user(username='Pete', email='pete@pete.com', password='password')
        sub = Subreddit.objects.create(name='hello', description='this is the description')
        Post.objects.create(title='arositenarsitearnst', description='aoirsetnarsoitenarsiot',
                            subreddit=sub, user=pete)
        Post.objects.create(title='This is title 2', description='This is the shit that I throw',
                            subreddit=sub, user=pete)

    def test_current_count(self):
        sub = Subreddit.objects.get(pk=1)
        self.assertEqual(sub.current_count(), 2)
        self.assertNotEqual(sub.current_count(), 25)

    def test_today_count(self):
        sub = Subreddit.objects.get(pk=1)
        self.assertEqual(sub.today_count(), 2)
        self.assertNotEquals(sub.today_count(), 25)

    def test_daily_average(self):
        sub = Subreddit.objects.get(pk=1)
        self.assertAlmostEqual(sub.daily_average(), 0.286, 2)
        self.assertNotEqual(sub.daily_average(), 5)


class TestPost(TestCase):

    def setUp(self):
        pete = User.objects.create_user(username='Pete', email='pete@pete.com', password='password')
        sub = Subreddit.objects.create(name='hello', description='this is the description')
        post = Post.objects.create(title='This is title 1', description='This post is awesome',
                                   subreddit=sub, user=pete)
        post2 = Post.objects.create(title='This is title 2', description='This is my test',
                                    subreddit=sub, user=pete)
        Comment.objects.create(user=pete, post=post2, comment_text='This is a dumb comment')
        Comment.objects.create(user=pete, post=post2, comment_text='This is a smart comment')
        Comment.objects.create(user=pete, post=post2, comment_text='This is the third comment')
        Comment.objects.create(user=pete, post=post2, comment_text='This is the fourth comment')
        Comment.objects.create(user=pete, post=post, comment_text='This is one comment')
        Comment.objects.create(user=pete, post=post, comment_text='This is two comment')
        PostUpVote.objects.create(post=post)
        PostUpVote.objects.create(post=post)
        PostUpVote.objects.create(post=post)
        PostDownVote.objects.create(post=post)

    def test_is_recent(self):
        post = Post.objects.get(pk=2)
        self.assertTrue(post.is_recent)

    def test_is_hot(self):
        post = Post.objects.get(title='This is title 1')
        post2 = Post.objects.get(pk=2)
        self.assertTrue(post2.is_hot())
        self.assertFalse(post.is_hot())

    def test_karma(self):
        post = Post.objects.get(pk=1)
        self.assertEquals(post.karma, 2)
        self.assertNotEqual(post.karma, 5)


class TestComment(TestCase):

    def test_karma(self):
        pete = User.objects.create_user(username='Pete', email='pete@pete.com', password='password')
        sub = Subreddit.objects.create(name='hello', description='this is the description')
        post = Post.objects.create(title='This is title 1', description='This post is so not hot',
                                   subreddit=sub, user=pete)
        comm = Comment.objects.create(user=pete, post=post, comment_text='This is a dumb comment')
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentDownVote.objects.create(comment=comm)
        CommentDownVote.objects.create(comment=comm)

        self.assertEqual(comm.karma, 3)
        self.assertNotEqual(comm.karma, 8)
