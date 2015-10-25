from django.contrib import admin
from .models import Subreddit, Post, Comment


@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url", "slug", "creation_time", "subreddit", "user")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "user", "post", "created_time")
