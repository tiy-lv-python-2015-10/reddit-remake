from django.contrib import admin
from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "post_karma", "comment_karma", "trophy_case", "average_good_karma", "average_bad_karma",
                    "total_count")
