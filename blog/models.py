from django.conf import settings
from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('blog:add_category')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, null=True, blank=True,)
    facebook_url = models.CharField(max_length=255, null=True, blank=True,)
    twitter_url = models.CharField(max_length=255, null=True, blank=True,)
    instagram_url = models.CharField(max_length=255, null=True, blank=True,)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True,)


    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse ('blog:index')

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to='images')
    post_body = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    category = models.CharField(max_length=100, default='uncategorized')
    snippet = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return str(self.post_title)+' | ' + str(self.post_author)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Comment(models.Model):
    post = models.ForeignKey(Post,  related_name='comments', on_delete=models.CASCADE)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='name')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.post_title, self.name)