from django.contrib import admin
from subreddit.models import Subreddit, Post, Comment, PostUpvote, CommentUpvote, Trophies


# Register your models here.
@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date_time')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'subreddit_rel', 'title', 'description', 'url', 'slug', 'creation_time', 'modification_time', 'is_recent',
    'num_upvotes', 'karma')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'created_time', 'modified_time')


@admin.register(PostUpvote)
class PostUpvoteAdmin(admin.ModelAdmin):
    list_display = ('post_upvotes', 'up_or_down', 'created_time')


@admin.register(CommentUpvote)
class CommentUpvoteAdmin(admin.ModelAdmin):
    list_display = ('comment_upvotes', 'up_or_down', 'created_time')

@admin.register(Trophies)
class TrophiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_time')
