from django.contrib import admin
from .models import Post, Feed, FeedFile,PostFile


# Register your models here.


class PostFileInline(admin.TabularInline):
    model = FeedFile


class FeedAdmin(admin.ModelAdmin):
    inlines = [
        PostFileInline,
    ]

class FeedFileInline(admin.TabularInline):
    model = PostFile


class PostAdmin(admin.ModelAdmin):
    inlines = [
        FeedFileInline,
    ]



admin.site.register(Post,PostAdmin)
admin.site.register(Feed,FeedAdmin)

