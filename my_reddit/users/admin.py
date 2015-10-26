from django.contrib import admin
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'post_karma', 'comm_karma', 'avg_up_votes', 'avg_down_votes', 'total_use')

