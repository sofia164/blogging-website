from django.contrib import admin

# Register your models here.

from .models import Post, Category, Profile, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ['post_title', 'post_body', 'pub_date',  'post_author']
    list_display = ('post_title', 'pub_date', 'was_published_recently', 'post_author')
    list_filter = (
        ('was_published_recently', admin.BooleanFieldListFilter),
    )
    search_fields = ['post_title','post_author']


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
