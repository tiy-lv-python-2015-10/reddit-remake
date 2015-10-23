from django.contrib import admin
from subreddit.models import Subreddit, Post, Comment


# Register your models here.
@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date_time')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'creation_time', 'modification_time')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_text', 'created_time', 'modified_time')
