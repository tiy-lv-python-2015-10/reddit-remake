from django.contrib import admin
from reddit.models import Subreddit, Post, Comment, PostUpVote, PostDownVote, CommentUpVote, CommentDownVote, Trophy


@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_on')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'url', 'slug', 'subreddit', 'user', 'karma',
                    'posted_at', 'modified_at')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'user', 'post', 'posted_at', 'modified_at')

@admin.register(PostUpVote)
class PostUpVoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'post_up_vote')

@admin.register(PostDownVote)
class PostDownVoteAdmin(admin.ModelAdmin):
    list_display = ('post', 'post_down_vote')

@admin.register(CommentUpVote)
class CommentUpVoteAdmin(admin.ModelAdmin):
    list_display = ('comment', 'comm_up_vote')

@admin.register(CommentDownVote)
class CommentDownVoteAdmin(admin.ModelAdmin):
    list_display = ('comment', 'comm_down_vote')

@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')