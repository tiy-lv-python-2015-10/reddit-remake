from django.contrib.auth.models import User
from django.test import TestCase
from reddit.models import PostUpVote, Comment, Subreddit, PostDownVote, CommentUpVote, CommentDownVote, Post
from users.models import Profile


class TestProfile(TestCase):
    def setup(self):
        dude = User.objects.create_user(username='Dude', email='pura@vida.com', password='password')
        sub = Subreddit.objects.create(name='hello', description='this is the description')
        Profile.objects.create(user=dude)
        post = Post.objects.create(title='This is title 2', description='This is the shit that I throw',
                                   subreddit=sub, user=dude)
        comm = Comment.objects.create(user=dude, subreddit=sub, comment_text='Vote or Die')
        PostUpVote.objects.create(post=post)
        PostUpVote.objects.create(post=post)
        PostUpVote.objects.create(post=post)
        PostDownVote.objects.create(post=post)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentUpVote.objects.create(comment=comm)
        CommentDownVote.objects.create(comment=comm)
        CommentDownVote.objects.create(comment=comm)

    def test_post_karma(self):
        """
        prof = Profile.objects.get(pk=1)
        self.assertEquals(prof.post_karma, 2)
        """
        pass

    def test_comm_karma(self):
        self.assertEquals(1, 1)

    def test_avg_up_votes(self):
        pass

    def test_avg_down_votes(self):
        pass

    def test_total_use(self):
        pass
