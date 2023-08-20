from django.contrib import admin
from .models import *
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
