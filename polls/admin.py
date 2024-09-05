from django.contrib import admin
from.models import Category, Comment, Post, Reyting, Banner, Settings

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Reyting)
admin.site.register(Banner)
admin.site.register(Settings)