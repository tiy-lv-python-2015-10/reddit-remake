from reddit.models import Post
from django.utils import timezone

# New: Chronologically newest to oldest
Post.objects.all().order_by('-posted_at')

# Hot: Ordered by amount of up-votes in the 3 hours
three_hours = timezone.now() - timezone.timedelta(hours=3)
hot = Post.objects.all().filter(posted_at__gte=three_hours)
sorted(hot, key=lambda x: x.postupvote_set.all().count(), reverse=True)

# Top: Highest rated for the last 24 hours
day = timezone.now() - timezone.timedelta(days=1)
top = Post.objects.all().filter(posted_at__gte=day)
top = sorted(top, key=lambda post: post.karma, reverse=True)

# Controversial: Ordered by posts with a high number of both up and down votes
