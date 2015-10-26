from django.contrib import admin
from reddits.models import Subreddit, Post, Comment, VotingSystem, Trophy


@admin.register(Subreddit)
class SubredditAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created", "current_count", "today_count", "daily_average")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "url", "slug", "karma", "creation_time", "subreddit", "user", "is_recent")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "user", "post", "karma", "created_time")


@admin.register(VotingSystem)
class VotingSystemAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "comment", "vote")

@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ("name",)